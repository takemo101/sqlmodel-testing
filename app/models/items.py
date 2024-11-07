from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Mail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: Optional[int] = None
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, nullable=False
    )
