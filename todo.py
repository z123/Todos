class Todo:
    def __init__(self, text):
        self.text = text
        self.childern = []

class TodoList:
    def __init__(self):
        self.todos = []

    def process(self, *args):
        todos = self.todos
        while len(args):
            found = False
            for i,todo in enumerate(todos):
                if todo.text == args[0] and len(args) == 1:
                    todos.pop(i)
                    return
                if todo.text == args[0]:
                    todos = todo.childern
                    args = args[1:]
                    found = True
                    break
            if not found:
                todo = Todo(args[0])
                todos.append(todo)
                todos = todo.childern
                args = args[1:]

def print_todos(todos, indent):
    for todo in todos:
        line = ' ' * indent + '- ' + todo.text
        print(line)
        print_todos(todo.childern, indent+2)

import os, sys, pickle
if os.path.isfile('todoDB.pkl'):
    todo_list = pickle.load(open('todoDB.pkl', 'rb'))
else:
    todo_list = TodoList()

if len(sys.argv[1:]):
    todo_list.process(*sys.argv[1:])
print_todos(todo_list.todos, 0)
pickle.dump(todo_list, open('todoDB.pkl', 'wb'))
