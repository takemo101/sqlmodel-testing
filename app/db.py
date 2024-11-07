from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Task(SQLModel, table=True):
    __tablename__ = 'tasks'  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str
    complete: bool = False


sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)
