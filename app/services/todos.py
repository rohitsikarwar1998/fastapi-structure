from schemas.todos import TodoItem
from utils.app_exceptions import AppException

from services.main import AppService, AppCRUD
from models.todos import Todos
from utils.service_result import ServiceResult


class TodoService(AppService):
    def create_item(self, item: TodoItem) -> ServiceResult:
        todo_item = TodoCRUD(self.db).create_item(item)
        if not todo_item:
            return ServiceResult(AppException.TodoCreateItem())
        return ServiceResult(todo_item)

    def get_item(self, item_id: int) -> ServiceResult:
        todo_item = TodoCRUD(self.db).get_item(item_id)
        if not todo_item:
            return ServiceResult(AppException.TodoGetItem({"item_id": item_id}))
        return ServiceResult(todo_item)


class TodoCRUD(AppCRUD):
    def create_item(self, item: TodoItem) -> TodoItem:
        todo_item = Todos(description=item.description, name=item.name)
        self.db.add(todo_item)
        self.db.commit()
        self.db.refresh(todo_item)
        return todo_item

    def get_item(self, item_id: int) -> TodoItem:
        todo_item = self.db.query(Todos).filter(Todos.id == item_id).first()
        if todo_item:
            return todo_item
        return None