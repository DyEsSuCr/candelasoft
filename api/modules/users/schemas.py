from sqlmodel import SQLModel
from typing import List, Optional
from datetime import datetime

from api.modules.countries.schemas import CountryRead


class Pagination(SQLModel):
    total_count: int
    limit: int
    offset: int
    total_pages: int
    current_page: int


class UserRead(SQLModel):
    id: int
    name: str
    email: str
    last_name: Optional[str]
    updated_at: datetime
    created_at: datetime
    country: Optional[CountryRead]


class UserReadPagination(SQLModel):
    data: List[UserRead]
    pagination: Pagination


class CombinedUserResponse(SQLModel):
    data: UserRead
    external_data: Optional[List[dict]]
    email_notification: Optional[dict] = None
