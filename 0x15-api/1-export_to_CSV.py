#!/usr/bin/python3
"""
Exports user tasks from JSONPlaceholder to
CSV based on provided user ID.
Usage: python3 1-export_to_CSV.py [user_id]
"""

import os
import requests
from sys import argv

def fetch_user_tasks(user_id):
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    tasks = tasks_response.json()

    users_response = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    users = users_response.json()

    username = next((user.get("username") for user in users if user.get("id") == int(user_id)), "")

    csv_filename = f"{user_id}.csv"

    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    with open(csv_filename, "a", encoding="utf-8") as csv_file:
        for task in tasks:
            if task.get("userId") == int(user_id):
                csv_file.write(f'"{user_id}","{username}","{task.get("completed")}","{task.get("title")}"\n')

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py [user_id]")
    else:
        fetch_user_tasks(argv[1])
