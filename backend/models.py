from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from database import Base

class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    amount = Column(Float)
    date= Column(DateTime)
    description=Column(String)
    category = Column(String, index=True)     
    merchantName=Column(String)
    # owner_id = Column(Integer)