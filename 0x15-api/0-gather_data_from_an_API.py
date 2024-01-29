#!/usr/bin/python3
"""
fetch data tasks by the user id
and display tasks completed/all
and who own this tasks
"""

import requests
import sys

if __name__ == "__main__":

    """ check for argv """
    if len(sys.argv) != 2:
        print('Using python3 file.py <userId>')
        sys.exit(1)

    """ fetch tasks and user """
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}').json()

    """ count the tasks """
    all_tasks = 0
    done_tasks = 0
    for task in todos:
        if task['userId'] == int(sys.argv[1]):
            if (task['completed']):
                done_tasks = done_tasks + 1
                all_tasks = all_tasks + 1
            else:
                all_tasks = all_tasks + 1

    """ print out tasks by the user """
    print(
        f"First line: Employee {
            user_name['name']} is done with tasks({done_tasks}/{all_tasks}):")
    for task in todos:
        if task['userId'] == int(sys.argv[1]) and task['completed']:
            print(f"\t{task['title']}")
