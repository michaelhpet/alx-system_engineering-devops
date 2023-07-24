#!/usr/bin/python3
"""Gather data from an API."""
import requests
import re
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Entry point to program."""
    user_id = argv[1]
    if not user_id or not re.fullmatch("\d+", user_id):
        return
    user_id = int(user_id)
    endpoint = BASE_URL + f"/users/{user_id}"
    employee = requests.get(endpoint).json()
    endpoint = BASE_URL + "/todos"
    todos = requests.get(endpoint).json()
    todos = list(filter(lambda x: x.get("userId") == user_id, todos))
    completed = list(filter(lambda x: x.get("completed"), todos))
    print(
        "Employee {:s} is done with tasks({:d}/{:d})".format(
            employee.get("name"),
            len(completed),
            len(todos)
        )
    )
    for todo in completed:
        print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    main()
