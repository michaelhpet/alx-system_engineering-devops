#!/usr/bin/python3
"""Gather data from an API."""
import csv
import re
import requests
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Entry point to program."""
    if len(argv) < 2 or not re.fullmatch(r"\d+", argv[1]):
        return
    user_id = int(argv[1])
    endpoint = BASE_URL + f"/users/{user_id}"
    employee = requests.get(endpoint).json()
    endpoint = BASE_URL + "/todos"
    todos = requests.get(endpoint, params={"userId": user_id}).json()
    completed = list(filter(lambda x: x.get("completed"), todos))
    with open(f"{user_id}.csv", "w") as file:
        f = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=f, quoting=csv.QUOTE_ALL)
        for todo in completed:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": employee.get("username"),
                "TASK_COMPLETED_STATUS": todo.get("completed"),
                "TASK_TITLE": todo.get("title")
            })


if __name__ == "__main__":
    main()
