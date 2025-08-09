from pydantic import BaseModel
from typing import Optional

class UserContext(BaseModel):
    user_name: Optional[str]
    account_number: Optional[str]
    balance: Optional[float] = 0.0
    authenticated: bool

class TransferContext(BaseModel):
    from_account: str
    to_account: str
    amount: float

class LoanContext(BaseModel):
    loan_type: str
    amount: float
    tenure_years: str

class RequestCallback(BaseModel):
    user_name: str
    issue: str
