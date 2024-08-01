#!/usr/bin/python3
"""3. Dictionary of list of dictionaries
mandatory
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(base_url)
    data = response.json()
    all_employees_task = {}
    for user in data:
        username = user["username"]
        employee_ID = user["id"]

        # print(employee_ID)
        todo_url = base_url + "/{}".format(employee_ID) + "/todos"
        user_todos_response = requests.get(todo_url)
        todos = user_todos_response.json()
        all_employees_task[employee_ID] = []

        for task in todos:
            all_employees_task[employee_ID].append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get("completed")
            })
# print(json_format)
        with open("todo_all_employees.json", "w") as filename:
            json.dump(all_employees_task, filename)
    # for task in todos:
    #     json_format[employee_ID].append({
    #            "task": task.get("title"),
    #            "completed": task.get("completed"),
    #            "username": username
    #     })
    # with open("{}.json".format(employee_ID), "w") as filename:
    #     json.dump(json_format, filename)
