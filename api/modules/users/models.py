from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, timezone


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    email: str = Field(max_length=255, sa_column_kwargs={'unique': True})
    last_name: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={'onupdate': 'CURRENT_TIMESTAMP'},
    )

    country_id: Optional[int] = Field(default=None, foreign_key='countries.id')
    country: Optional['Country'] = Relationship(back_populates='users')
