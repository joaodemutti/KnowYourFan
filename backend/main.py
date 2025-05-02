from fastapi import FastAPI
from app.api.users import users_routes
from app.api.documents import documents_routes
from app.api.auth import auth_routes
from app.api.esports import esports_routes
from fastapi.middleware.cors import CORSMiddleware
import os

origin = os.getenv("FRONTEND_ORIGIN")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_routes.router)
app.include_router(documents_routes.router)
app.include_router(auth_routes.router)
app.include_router(esports_routes.router)
