from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from api.database import get_session

from .schemas import UserReadPagination, CombinedUserResponse
from .services import user_service

router = APIRouter()


@router.get('', response_model=UserReadPagination)
async def find_all(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=5, ge=5, le=100),
    db: Session = Depends(get_session),
):
    return await user_service.get_all(page, limit, db)


@router.get('/{user_id}', response_model=CombinedUserResponse)
async def find_one(user_id: int, db: Session = Depends(get_session)):
    return await user_service.get_by_id(db, user_id)
