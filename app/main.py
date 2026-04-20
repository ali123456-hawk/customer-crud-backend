from fastapi import FastAPI
from .database import Base, engine
from .routes import customer

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Customer CRUD API")

app.include_router(customer.router)