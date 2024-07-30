#!/usr/bin/python3
"""0. Gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    employee_ID = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    complete_url = base_url + "/" + employee_ID

    response = requests.get(complete_url)
    employee_name = response.json().get("name")
    completed_tasks = []
    completed = 0
    todo_url = complete_url + "/todos"
    user_todos_response = requests.get(todo_url)
    todos = user_todos_response.json()
    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task)
            completed = completed + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed, len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
