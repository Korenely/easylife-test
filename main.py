from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_admin.contrib.sqla import Admin

from database import engine, Base
from admin import StatisticsView, UserView, TransactionView
from models import Transaction, User

import user_controller
import transaction_controller


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_controller.router, tags=["user controllers"])
app.include_router(transaction_controller.router, tags=["transaction controllers"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


admin = Admin(
    engine,
    title="EasyLife",
    index_view=StatisticsView(label="Home")
)

admin.add_view(UserView(User))
admin.add_view(TransactionView(Transaction))


admin.mount_to(app)
