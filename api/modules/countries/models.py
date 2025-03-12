from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone


class Country(SQLModel, table=True):
    __tablename__ = 'countries'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    iso_code: str = Field(max_length=3)
    iso_code_alpha_3: str = Field(max_length=3)
    indicative: str = Field(max_length=3)
    currency: str = Field(max_length=3)
    currency_symbol: str = Field(max_length=3)
    time_zone: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={'onupdate': 'CURRENT_TIMESTAMP'},
    )

    users: List['User'] = Relationship(back_populates='country')
