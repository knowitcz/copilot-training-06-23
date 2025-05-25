from fastapi import Depends
from sqlmodel import Session
from app.db import get_session
from app.repository.account_repository import AccountRepository
from app.services.account_service import AccountService
from app.services.bank_service import OnlineBankService
from app.validator.amount_validator import AmountValidator

def get_account_repository(session: Session = Depends(get_session)) -> AccountRepository:
    return AccountRepository(session)

def get_online_bank_service(
    repo: AccountRepository = Depends(get_account_repository)
) -> OnlineBankService:
    account_service = AccountService(repo)
    amount_validator = AmountValidator()
    return OnlineBankService(account_service, amount_validator)
