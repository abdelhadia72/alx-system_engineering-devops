#!/usr/bin/python3
"""
Exports user tasks from JSONPlaceholder to
CSV based on provided user ID.
Usage: python3 1-export_to_CSV.py [user_id]
"""

import os
from requests import get
from sys import argv


def fetch_user_tasks(user_id):
    tasks_res = get(f'https://jsonplaceholder.typicode.com/todos/')
    tasks = tasks_res.json()

    users_response = get(f'https://jsonplaceholder.typicode.com/users/')
    users = users_response.json()

    username = next(
        (user.get("username")
            for user in users
            if user.get("id") == int(user_id)),
        ""
    )

    csv_filename = f"{user_id}.csv"

    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    with open(csv_filename, "a", encoding="utf-8") as f:
        for task in tasks:
            completed = task.get("completed")
            title = task.get("title")
            if task.get("userId") == int(user_id):
                f.write(f'"{user_id}","{username}","{completed}","{title}"\n')


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py [user_id]")
    else:
        fetch_user_tasks(argv[1])
