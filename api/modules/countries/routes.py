from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from api.database import get_session

from .schemas import CountryReadPagination
from .services import country_service

router = APIRouter()


@router.get('', response_model=CountryReadPagination)
def find_all(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=5, ge=5, le=100),
    db: Session = Depends(get_session),
):
    return country_service.get_all(page, limit, db)
