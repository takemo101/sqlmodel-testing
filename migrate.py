from sqlmodel import SQLModel

from app.db import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  # モデルからテーブルを生成


if __name__ == '__main__':
    create_db_and_tables()
