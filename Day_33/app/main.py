from fastapi.templating import Jinja2Templates
from fastapi import Request, WebSocket, FastAPI, Depends, HTTPException, WebSocketDisconnect
from typing import List
from contextlib import asynccontextmanager
from database import async_session, init_db
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from models import Notification
from schemas import NotificationCreate, NotificationRead
from fastapi.staticfiles import StaticFiles
from sqlalchemy import insert, select

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[Request] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """
        Send a message to all connected WebSocket clients.
        Message is a dictionary that will be converted to JSON.
        """
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                disconnected.append(connection)
        for connection in disconnected:
            self.disconnect(connection)

manager = ConnectionManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/notifications", response_model=List[NotificationRead])
async def list_notifications(session: AsyncSession = Depends(get_session)):
    stmt = select(Notification).order_by(Notification.id.desc()).limit(7)
    result = await session.execute(stmt)
    notification = result.scalars().all()
    return notification


# --- POST Request Methods ---
@app.post("/notifications", response_model=NotificationRead)
async def create_notification(
    notif: NotificationCreate,
    session: AsyncSession = Depends(get_session)
):
    stmt = insert(Notification).values(
        user_id = notif.user_id,
        message = notif.message
    ).returning(Notification)

    result = await session.execute(stmt)
    new_notif = result.scalar_one()
    await session.commit()

    message_to_broadcast = {
        "action" : "new_notification",
        "data" : {
            "id": new_notif.id,
            "user_id": new_notif.user_id,
            "message": new_notif.message
        }
    }
    await manager.broadcast(message_to_broadcast)

    return new_notif

# --- WebSockets Endpoints ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except WebSocketDisconnect:
        manager.disconnect(websocket)