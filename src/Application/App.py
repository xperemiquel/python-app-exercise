from src.Services.TodoService import TodoService


class App:
    def __init__(self):
        self._todo_service = TodoService()

    def todo_service(self) -> TodoService:
        return self._todo_service
