from fastapi import FastAPI
from app.api.user import user_routes
from app.api.document import document_routes
from app.api.auth import auth_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(document_routes.router)
app.include_router(auth_routes.router)
