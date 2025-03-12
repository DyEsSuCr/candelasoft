from sqlmodel import SQLModel
from typing import List
from datetime import datetime


class Pagination(SQLModel):
    total_count: int
    limit: int
    offset: int
    total_pages: int
    current_page: int


class CountryRead(SQLModel):
    id: int
    name: str
    iso_code: str
    iso_code_alpha_3: str
    indicative: str
    currency: str
    currency_symbol: str
    time_zone: str
    created_at: datetime
    updated_at: datetime


class CountryReadPagination(SQLModel):
    data: List[CountryRead]
    pagination: Pagination
