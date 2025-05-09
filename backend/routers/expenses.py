from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine, Base
from models import Expenses
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import verify_token



router = APIRouter(prefix="/expenses", tags=["expenses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ExpenseRequest(BaseModel):
    category : str
    amount : float
    date : datetime
    description:str

class ExpenseOut(ExpenseRequest):
    id: int  # include ID in responses

    class Config:
        from_attributes  = True

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ExpenseOut)
async def create_expense(
        expense_request: ExpenseRequest,
        user_id: str = Depends(verify_token),
        db: Session = Depends(get_db)
):
    new_expense = Expenses(**expense_request.model_dump(), user_id=user_id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


# Get all expenses
@router.get("/", response_model=List[ExpenseOut])
async def get_all_expenses(user_id: str = Depends(verify_token),
        db: Session = Depends(get_db)
):
    return db.query(Expenses).filter(Expenses.user_id == user_id).all()  # Get all expenses

# Update an expense
@router.put("/{expense_id}")
async def update_expense(
        expense_id: int,
        expense_data: ExpenseRequest,
        user_id: str = Depends(verify_token),
        db: Session = Depends(get_db)
):
    existing_expense = db.query(Expenses).filter(Expenses.id == expense_id, Expenses.user_id == user_id).first()    
    if not existing_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    for key, value in expense_data.model_dump().items():
        setattr(existing_expense, key, value)

    db.commit()
    db.refresh(existing_expense)
    return existing_expense


# Delete an expense
@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(
        expense_id: int,
        user_id: str = Depends(verify_token),
        db: Session = Depends(get_db)
):
    expense = db.query(Expenses).filter(Expenses.id == expense_id, Expenses.user_id == user_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}
