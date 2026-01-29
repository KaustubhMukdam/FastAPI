from pydantic import BaseModel, Field
from typing import List, Optional

class Income(BaseModel):
    source: str
    amount: float
    frequency: str = Field(..., description="Frequency of income (e.g., monthly, yearly bi-weekly)")

class Expense(BaseModel):
    category: str
    amount: float
    frequency: str = Field(..., description="Frequency of expense (e.g., monthly, yearly bi-weekly)")
    essential: bool = Field(..., description="Indicates if the expense is essential or non-essential")

class Debt(BaseModel):
    type: str
    amount: float
    interest_rate: float = Field(..., description="Annual interest rate as a percentage")
    minimum_payment: float

class FinancialProfile(BaseModel):
    monthly_income: List[Income]
    monthly_expenses: List[Expense]
    debts: List[Debt]
    savings: float = Field(..., description="Total savings amount")
    emergency_fund: Optional[float] = Field(0, description="Amount set aside for emergencies")
    retirement_savings: Optional[float] = Field(0, description="Amount saved for retirement")
    credit_score: Optional[int] = Field(None, description="Credit score of the individual")

class FinancialReportResult(BaseModel):
    financial_advice: str = Field(..., description="Personalized financial advice based on the user's profile")
    debt_to_income_ratio: str = Field(..., description="Debt-to-Income ratio as a percentage")
    risk: int = Field(..., description="Risk assessment score from 1 (low risk) to 10 (high risk)", ge=1, le=10)
    decrease_risk: str = Field(..., description="Suggestions to decrease financial risk")