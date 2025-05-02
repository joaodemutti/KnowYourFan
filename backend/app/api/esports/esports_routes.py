from fastapi import APIRouter,Depends
from app.api.auth.dependency import get_current_user
from app.api.esports.queries.get_esports import GetEsportsHandler

router = APIRouter()

@router.get("/esports")
async def get_esports(user_id: str =  Depends(get_current_user)):
    handler = GetEsportsHandler(user_id=user_id)
    return await handler.handle()