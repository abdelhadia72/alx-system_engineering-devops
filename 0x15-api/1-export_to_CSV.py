"""
This script exports user tasks from the JSONPlaceholder API to a CSV file.
The script takes a user ID as a command-line argument and retrieves the tasks associated with that user.
It then creates a CSV file with the following columns: "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE".
Each row in the CSV file represents a task associated with the specified user.

Usage: python3 1-export_to_CSV.py [user_id]
"""

from requests import get
from sys import argv
import os

# Rest of the code...
#!/usr/bin/python3


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
