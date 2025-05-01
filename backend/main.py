from fastapi import FastAPI
from app.api.user import user_routes
from app.api.document import document_routes
from app.api.auth import auth_routes
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://knowyourfan.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_routes.router)
app.include_router(document_routes.router)
app.include_router(auth_routes.router)
