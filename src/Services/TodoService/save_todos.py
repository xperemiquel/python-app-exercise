import csv
from datetime import date

def save_todos(response, path):
    for todo in response:
        save_todo_into_csv(todo, path)


def save_todo_into_csv(todo, path):
    filename = generate_filename(todo, path)
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(todo))
            writer.writeheader() # We could just remove this line if we don't want to write the headers
            writer.writerow(todo)
    except IOError:
        print("I/O error")


def generate_filename(todo, path):
    date_str = date.today().strftime("%Y_%m_%d")
    return f"{path}{date_str}_{todo['id']}.csv"




