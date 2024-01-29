#!/usr/bin/python3
"""
Exports All user's tasks into a JSON
file based
Usage: python3 1-export_to_JSON.py [user_id]
"""

from requests import get
from sys import argv
import json


def fetch_user_tasks():
    tasks_res = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = tasks_res.json()

    users_response = get('https://jsonplaceholder.typicode.com/users/')
    users = users_response.json()

    data = {}
    for user in users:
        user_id = user.get("id")
        user_tasks = []
        for task in tasks:
            if task.get("userId") == user_id:
                task_info = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")
                }
                user_tasks.append(task_info)
        data[user_id] = user_tasks

    json_filename = "todo_all_employees.json"

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    fetch_user_tasks()
