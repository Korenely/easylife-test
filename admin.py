from fastapi import Request
from starlette_admin import CustomView
from models import Transaction
from database import SessionLocal
from sqlalchemy import func
from datetime import datetime
from starlette.templating import Jinja2Templates
from starlette_admin.contrib.sqla import ModelView


class UserView(ModelView):
    fields = ["id", "username"]


class TransactionView(ModelView):
    fields = ["id", "user", "transaction_type", "amount"]


class StatisticsView(CustomView):

    async def render(self, request: Request, templates: Jinja2Templates):

        db = SessionLocal()
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        query = db.query(Transaction)

        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            query = query.filter(Transaction.created_at >= start_date)
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            query = query.filter(Transaction.created_at <= end_date)

        total_transactions = query.count()
        total_amount = (
            db.query(func.sum(Transaction.amount)).filter(query.exists()).scalar() or 0
        )

        db.close()

        return templates.TemplateResponse(
            request,
            "statistics.html",
            context={
                "total_transactions": total_transactions,
                "total_amount": total_amount,
                "start_date": start_date if start_date else "",
                "end_date": end_date if end_date else "",
            },
        )
