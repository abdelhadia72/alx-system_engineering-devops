#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def fetch_tasks(user_id):
    """Fetch tasks from the API based on user ID."""
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    return todos, user_name


def count_tasks(todos, user_id):
    """Count completed and all tasks for the user."""
    all_tasks = 0
    done_tasks = 0
    for task in todos:
        if task.get('userId') == user_id:
            if task.get('completed'):
                done_tasks += 1
            all_tasks += 1
    return all_tasks, done_tasks


def print_tasks(user_name, all_tasks, done_tasks, todos):
    """Print tasks completed by the user."""
    print(
        f"Employee {
            user_name.get('name')} is done with tasks({done_tasks}/{all_tasks}):")
    for task in todos:
        if task.get('userId') == user_id and task.get('completed'):
            print(f"\t{task.get('title')}")


if __name__ == "__main__":
    """Check for argv."""
    if len(sys.argv) != 2:
        print('Usage: python3 file.py <userId>')
        sys.exit(1)

    user_id = int(sys.argv[1])
    todos, user_name = fetch_tasks(user_id)
    all_tasks, done_tasks = count_tasks(todos, user_id)
    print_tasks(user_name, all_tasks, done_tasks, todos)
d
