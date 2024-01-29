#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    r1 = get('https://jsonplaceholder.typicode.com/todos/')
    data = r1.json()
    done_tasks = 0
    all_tasks = 0
    tasks = []
    r1 = get('https://jsonplaceholder.typicode.com/users')
    data2 = r1.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            user = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            all_tasks += 1

            if i.get('completed') is True:
                done_tasks += 1
                tasks.append(i.get('title'))

    print(f"Employee {user} is done with tasks({done_tasks}/{all_tasks}):")

    for i in tasks:
        print("\t {}".format(i))
