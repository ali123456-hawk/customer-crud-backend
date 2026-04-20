from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/customers", tags=["Customers"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)


@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return crud.get_customers(db)


@router.get("/{customer_id}")
def read_one(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_customer(db, customer_id)


@router.put("/{customer_id}")
def update(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    return crud.update_customer(db, customer_id, customer)


@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    return crud.delete_customer(db, customer_id)