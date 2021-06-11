from sys import stderr
from .settings import STORAGE_PATH, URL
from .load_todos import load_todos
from .save_todos import save_todos

class TodoService:
    def __init__(self):
        self.url = URL
        self.storage_path = STORAGE_PATH

    def run(self):
        print('Running TodoService', file=stderr)
        loaded_todos = load_todos(self.url)
        save_todos(loaded_todos, self.storage_path)
        print('TodoService finished successfully', file=stderr)
