import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

load_dotenv()  # Load environment variables from .env

router = APIRouter(prefix="/expensesummary", tags=["todos"])

# Define the Pydantic model for request validation
class ReceiptData(BaseModel):
    amount: float
    date: str
    description: str
    merchantName: str
    category: str

# Async function to generate a professional expense summary
async def generate_summary(receipt_data):
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise Exception("Missing GOOGLE_API_KEY environment variable")

        # Configure Gemini API
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        prompt = f"""
        Generate a concise 4-5 line summary of the following expense for an expense report:

        Amount: ${receipt_data["amount"]}
        Date: {receipt_data["date"]}
        Description: {receipt_data["description"]}
        Merchant: {receipt_data["merchantName"]}
        Category: {receipt_data["category"]}

        Make the summary professional, highlighting the key details of the purchase, its business purpose,
        and why it might be a necessary expense. Keep it objective and informative.

        DO NOT use bullet points or numbered lists. Write it as 4-5 continuous text lines with proper spacing.
        DO NOT include the title "Expense Summary" or any headings.
        DO NOT mention that this is an "expense report" - just provide the summary directly.
        """

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating expense summary: {str(e)}")

# FastAPI endpoint
@router.post("/generate_expense_summary/")
async def generate_expense_summary_endpoint(receipt_data: ReceiptData):
    summary = await generate_summary(receipt_data.dict())
    return {"summary": summary}
