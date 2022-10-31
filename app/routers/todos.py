from fastapi import APIRouter, Depends
from services.todos import TodoService
from schemas.todos import TodoItem
from utils.service_result import handle_result
from config.database import SessionFactory
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/todo",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/item/", response_model=TodoItem)
async def create_item(item: TodoItem, SessionFactory: Session = Depends(SessionFactory)):
    with SessionFactory.get_session() as db:
        result = TodoService(db).create_item(item)
    return handle_result(result)

@router.get("/item/{item_id}", response_model=TodoItem)
async def get_item(item_id: int, SessionFactory: Session = Depends(SessionFactory)):
    with SessionFactory.get_session() as db:
        result = TodoService(db).get_item(item_id)
    return handle_result(result)