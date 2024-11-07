from fastapi import APIRouter
from sqlmodel import Session, select

from app.db import Task, engine

tasks_router = APIRouter()


@tasks_router.get('/tasks', response_model=list[Task])
async def tasks() -> list[Task]:
    response: list[Task] = []

    with Session(engine) as session:
        stmt = select(Task)
        results = session.exec(stmt)
        for task in results:
            response.append(task)

    return response


@tasks_router.get('/tasks/create', response_model=Task)
async def create_task() -> Task:
    task = Task(name='Task1', status='todo')

    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        # session.close() with ステートメントを使っているのでcloseが不要になる

    return task
