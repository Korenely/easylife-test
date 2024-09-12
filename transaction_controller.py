from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import User, Transaction
from schemas import TransactionCreate
from database import get_db

router = APIRouter()


@router.post("/transaction/")
def add_transaction(
    user_id: int, transaction: TransactionCreate, db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_transaction = Transaction(
        user_id=user_id,
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return {
        "id": db_transaction.id,
        "user_id": db_user.id,
        "amount": db_transaction.amount,
    }
