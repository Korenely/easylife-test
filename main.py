from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from database import engine, Base
from admin import StatisticsAdmin
from models import User, Transaction

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
    title="Admin Panel",
    index_view=StatisticsAdmin(label="Home")
)

admin.add_view(ModelView(User))
admin.add_view(ModelView(Transaction))


admin.mount_to(app)
