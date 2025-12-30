from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models
from . import schemas
from . import database

app = FastAPI()


@app.get("/drivers/", response_model=List[schemas.F1data])
def get_all_drivers(db: Session = Depends(database.get_db)):
    return db.query(models.F1data).all()


@app.get("/drivers/{driver_id}", response_model=schemas.F1data)
def get_driver_by_id(driver_id: int, db: Session = Depends(database.get_db)):
    driver = db.query(models.F1data).filter(models.F1data.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found.")
    return driver


@app.post("/drivers/", response_model=schemas.F1data, status_code=status.HTTP_201_CREATED)
def create_driver(driver: schemas.F1dataCreate, db: Session = Depends(database.get_db)):
    db_driver = models.F1data(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


@app.put("/drivers/{driver_id}", response_model=schemas.F1data)
def update_driver(driver_id: int, driver_in: schemas.F1dataCreate, db: Session = Depends(database.get_db)):
    driver = db.query(models.F1data).filter(models.F1data.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found.")
    for key, value in driver_in.dict().items():
        setattr(driver, key, value)
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver


@app.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(database.get_db)):
    driver = db.query(models.F1data).filter(models.F1data.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found.")
    db.delete(driver)
    db.commit()
    return {"detail": "Driver deleted successfully."}