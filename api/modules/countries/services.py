from sqlmodel import Session, select, func
from api.database import get_session
from fastapi import Query, Depends

from .models import Country
from .schemas import CountryReadPagination


class CountryService:
    def get_all(
        self,
        page: int = Query(default=1, ge=1),
        limit: int = Query(default=5, ge=5, le=100),
        db: Session = Depends(get_session),
    ) -> CountryReadPagination:
        offset = (page - 1) * limit

        total = db.exec(func.count(Country.id)).scalar()

        statement = select(Country).offset(offset).limit(limit)
        result = db.exec(statement).all()

        total_pages = (total + limit - 1) // limit

        return {
            'data': result,
            'pagination': {
                'total_count': total,
                'limit': limit,
                'offset': offset,
                'total_pages': total_pages,
                'current_page': page,
            },
        }


country_service = CountryService()
