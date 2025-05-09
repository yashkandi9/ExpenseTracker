import base64
import json
import os
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, status
from dotenv import load_dotenv
import google.generativeai as genai
from sqlalchemy.orm import Session
from datetime import datetime
from database import SessionLocal
from models import Expenses
from typing import Annotated

router = APIRouter(prefix="/receiptscanner", tags=["receipts"])



# Load environment variables
load_dotenv()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Async receipt scanning function
async def scan_receipt(file: UploadFile):
    try:
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY is missing in environment variables")

        # Configure Gemini API
        genai.configure(api_key=api_key)

        # Initialize model
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        # Read file content
        file_content = await file.read()
        base64_data = base64.b64encode(file_content).decode('utf-8')
        mime_type = file.content_type

        # Prompt
        prompt = '''
        Analyze this receipt image and extract the following information in JSON format:
        - Total amount (just the number)
        - Date (in ISO format)
        - Description or items purchased (brief summary)
        - Merchant/store name
        - Suggested category (one of: housing, transportation, groceries, utilities, entertainment, food, shopping, healthcare, education, personal, travel, insurance, gifts, bills, other-expense)

        Only respond with valid JSON in this exact format:
        {
          "amount": number,
          "date": "ISO date string",
          "description": "string",
          "merchantName": "string",
          "category": "string"
        }
        If this is not a receipt, return { "isReceipt": false }
        '''

        # Prepare input parts
        parts = [
            {
                "inline_data": {
                    "data": base64_data,
                    "mime_type": mime_type
                }
            },
            prompt
        ]

        # Get model response
        response = model.generate_content(parts)
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()

        # Parse JSON
        data = json.loads(cleaned_text)

        if data.get("isReceipt") is False:
            return {"isReceipt": False}

        return {
            "amount": float(data.get("amount", 0)),
            "date": data.get("date"),
            "description": data.get("description", ""),
            "category": data.get("category", "other-expense"),
            "merchantName": data.get("merchantName", ""),
            "isReceipt": True
        }

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {str(e)}")
        print(f"Response text: {response.text}")
        raise HTTPException(status_code=500, detail="Failed to parse receipt data")
    except Exception as e:
        print(f"Error scanning receipt: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error scanning receipt: {str(e)}")

# FastAPI route with expense creation
@router.post("/scan_receipt/")
async def scan_receipt_endpoint(
    # db: Session = Depends(get_db),
    file: UploadFile = File(...)
):

    
    # Scan the receipt
    receipt_data = await scan_receipt(file)
    
    # # If it's a valid receipt, create an expense entry
    # if receipt_data.get("isReceipt", False):
    #     try:
    #         # Convert receipt data to expense entry
    #         new_expense = Expenses(
    #             amount=receipt_data["amount"],
    #             date=datetime.fromisoformat(receipt_data["date"]),
    #             description=receipt_data["description"],
    #             category=receipt_data["category"],
    #             merchantName=receipt_data["merchantName"],
                
    #         )
            
    #         # Add to database
    #         db.add(new_expense)
    #         db.commit()
    #         db.refresh(new_expense)
            
    #         # Add expense ID to the response
    #         receipt_data["expense_id"] = new_expense.id
    #         receipt_data["message"] = "Expense entry created successfully"
            
    #     except Exception as e:
    #         # If expense creation fails, still return receipt data but with error message
    #         print(f"Error creating expense entry: {str(e)}")
    #         receipt_data["expense_created"] = False
    #         receipt_data["error"] = f"Receipt scanned successfully but expense creation failed: {str(e)}"
    
    return receipt_data