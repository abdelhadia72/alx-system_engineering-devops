#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    tasks = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = tasks.json()
    user_name = get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user_name = user_name.json()
    done_tasks = 0
    all_tasks = 0
    list_of_tasks = []

    for task in tasks:
        if task.get('userId') == int(argv[1]):
            if (task.get('completed') is True):
                list_of_tasks.append(task)
                all_tasks += 1
                done_tasks += 1
            else:
                all_tasks += 1

    print(f"Employee {user_name.get("name")
                      } is done with tasks({done_tasks}/{all_tasks}):")

    for task in list_of_tasks:
        print(f"\t {task.get('title')}")
