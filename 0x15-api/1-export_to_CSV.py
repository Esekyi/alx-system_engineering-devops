#!/usr/bin/python3
"""1. Export to CSV"""

import requests
import sys


if __name__ == "__main__":
    employee_ID = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    complete_url = base_url + "/" + employee_ID

    response = requests.get(complete_url)
    username = response.json().get("username")

    todo_url = complete_url + "/todos"
    user_todos_response = requests.get(todo_url)
    todos = user_todos_response.json()

    with open("{}.csv".format(employee_ID), "w") as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_ID, username, task.get("completed"),
                               task.get("title")))
