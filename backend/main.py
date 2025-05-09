from fastapi import FastAPI, Depends
from models import Expenses
from database import SessionLocal, engine, Base
from routers import auth, expenses, expense_summary, receipt_scanner
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routers.auth import verify_token
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


app = FastAPI()

# Allow requests from your frontend (adjust the origin if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(expense_summary.router)
app.include_router(receipt_scanner.router)


@app.get("/")
def read_root():
    return {"message": "Expenses Fast API"}
