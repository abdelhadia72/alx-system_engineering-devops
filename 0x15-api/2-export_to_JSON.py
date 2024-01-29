#!/usr/bin/python3
"""
Exports user tasks from APi to
Json file based on provided user ID.
Usage: python3 1-export_to_JSON.py [user_id]
"""

from requests import get
from sys import argv
import json


def fetch_user_tasks(user_id):
    tasks_res = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = tasks_res.json()

    users_response = get('https://jsonplaceholder.typicode.com/users/')
    users = users_response.json()

    username = next(
        (user.get("username")
            for user in users
            if user.get("id") == int(user_id)),
        ""
    )

    data = {user_id: []}
    for task in tasks:
        if task.get("userId") == int(user_id):
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            data[user_id].append(task_info)

    json_filename = f"{user_id}.json"

    with open(json_filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py [user_id]")
    else:
        fetch_user_tasks(argv[1])
