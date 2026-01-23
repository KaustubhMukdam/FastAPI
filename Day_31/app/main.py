from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from typing import List
from contextlib import asynccontextmanager

from database import async_session, get_db
from models import Product
from schemas import ProductCreate, ProductRead
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_db()
    yield

app = FastAPI(lifespan=lifespan)

# --- API Endpoints ---


# --- GET Request Methods ---
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI + Neon Demo"}

@app.get("/products", response_model=List[ProductRead])
async def listProducts(session: AsyncSession = Depends(get_session)):
    stmt = select(Product)
    result = await session.execute(stmt)
    products = result.scalars().all()
    return products

@app.get("/products/{product_id}", response_model=ProductRead)
async def getProduct(product_id: int, session: AsyncSession = Depends(get_session)):
    stmt = select(Product).where(Product.id == product_id)
    result = await session.execute(stmt)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# --- POST Request Methods ---
@app.post("/products", response_model=ProductRead)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_session),
):
    stmt = insert(Product).values(name=product.name, price=product.price).returning(Product)
    result = await session.execute(stmt)
    new_product = result.scalar_one_or_none()

    if not new_product:
        raise HTTPException(status_code=400, detail="Product not created")
    
    await session.commit()
    return new_product

