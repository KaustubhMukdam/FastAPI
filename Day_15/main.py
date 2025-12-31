from typing import Annotated, List
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from sqlmodel import Field, SQLModel, Session, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

load_dotenv()

# Async database setup (moved before lifespan)
DATABASE_URL = os.getenv("DAY_15_DATABASE_URL")  # Fixed typo: DATBASE -> DATABASE
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # Use conn.run_sync() to run synchronous SQLModel metadata creation
        await conn.run_sync(SQLModel.metadata.create_all)

    yield   # Yield control back to the application

    # Shutdown tasks
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

# Models
class ItemBase(SQLModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase, table=True):
    id: int = Field(default=None, primary_key=True)

class ItemRead(ItemBase):
    id: int

# Service layer
class ItemService:
    async def create_item(self, item: ItemCreate, db: AsyncSession) -> Item:
        db_item = Item(name=item.name, description=item.description)
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item
    
    async def get_item(self, item_id: int, db: AsyncSession) -> Item:
        statement = select(Item).where(Item.id == item_id)
        result = await db.execute(statement)
        item = result.scalar_one_or_none()
        return item
        
    async def get_items(self, db: AsyncSession) -> List[Item]:
        statement = select(Item)
        result = await db.execute(statement)
        items = result.scalars().all()
        return items
        
# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

def get_item_service():
    return ItemService()

db_dependency = Annotated[AsyncSession, Depends(get_db)]
item_service_dependency = Annotated[ItemService, Depends(get_item_service)]

# --- API Endpoints ---

# --- GET Request Methods ---

@app.get("/items/", response_model=List[ItemRead])
async def read_items(db: db_dependency, item_service: item_service_dependency):
    items = await item_service.get_items(db)
    return items

@app.get("/items/{item_id}", response_model=ItemRead)
async def read_item(item_id: int, db: db_dependency, item_service: item_service_dependency):
    item = await item_service.get_item(item_id, db)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# --- POST Request Methods ---
@app.post("/items/", response_model=ItemRead)
async def create_item(item: ItemCreate, background_tasks: BackgroundTasks, item_service: item_service_dependency, db: db_dependency):
    created_item = await item_service.create_item(item, db)
    background_tasks.add_task(log_operation, created_item.id)
    return created_item

async def log_operation(item_id: int):
    # Simulate logging operation
    print(f"Item with ID {item_id} has been created.")