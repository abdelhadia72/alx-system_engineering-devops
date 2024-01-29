#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import os

if __name__ == "__main__":
    r1 = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = r1.json()
    r1 = get(f'https://jsonplaceholder.typicode.com/users/{int(argv[1])}')
    user = r1.json()

    if os.path.exists and os.path.isfile(f"{argv[1]}.csv"):
        os.remove(f"{argv[1]}.csv")

    with open(f"{argv[1]}.csv", "a", encoding="utf-8") as f:
        for task in tasks:
            if task.get("userId") == int(argv[1]):
                f.write(f'"{argv[1]}","{user.get("username")}","{
                        task.get("completed")}","{task.get("title")}"\n')

"""
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"2","Antonette","False","laborum aut in quam"
"""
