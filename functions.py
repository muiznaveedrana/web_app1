def get_todos(filename = "todos.txt"):

    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filename = "todos.txt"):
    with open(filename, 'w') as file:
        file.writelines(todos)
