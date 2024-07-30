#!/usr/bin/python3
"""2. Export to JSON"""

import json
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
    json_format = {employee_ID: []}

    for task in todos:
        json_format[employee_ID].append({
               "task": task.get("title"),
               "completed": task.get("completed"),
               "username": username
        })
    with open("{}.json".format(employee_ID), "w") as filename:
        json.dump(json_format, filename)
