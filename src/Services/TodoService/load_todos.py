from requests import get

def load_todos(url):
    return get(url).json()
