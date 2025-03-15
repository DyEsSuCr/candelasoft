from sqlmodel import Session, select, func
from fastapi import Query, Depends, HTTPException
import httpx

from .models import User
from .schemas import UserReadPagination

from api.database import get_session
from api.utils.send_email import simulate_email_notification
from api.config import settings


class UserService:
    async def get_all(
        self,
        page: int = Query(default=1, ge=1),
        limit: int = Query(default=5, ge=5, le=100),
        db: Session = Depends(get_session),
    ) -> UserReadPagination:
        offset = (page - 1) * limit

        total = db.exec(func.count(User.id)).scalar()

        statement = select(User).offset(offset).limit(limit)
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

    async def get_by_id(self, db: Session, user_id: int):
        user = db.get(User, user_id)
        email_notification = None

        if not user:
            raise HTTPException(status_code=404, detail='Usuario no encontrado')

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f'{settings.EXTERNAL_API_URL}/todos?userId={user_id}'
                )
            response.raise_for_status()
            external_data = response.json()

            if external_data[0]['completed']:
                reason = 'tienes publicaciones inactivas que requieren tu atención'
                email_notification = simulate_email_notification(user, reason)

        except httpx.HTTPStatusError:
            external_data = {'error': 'API externa no disponible'}

        result = {
            'data': user,
            'external_data': external_data,
        }

        if email_notification:
            result['email_notification'] = email_notification

        return result


user_service = UserService()
