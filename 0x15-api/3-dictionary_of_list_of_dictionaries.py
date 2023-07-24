#!/usr/bin/python3
"""Gather data from an API."""
import json
import re
import requests
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Entry point to program."""
    endpoint = BASE_URL + f"/users"
    employees = requests.get(endpoint).json()
    out_dict = {}
    for employee in employees:
        endpoint = BASE_URL + f"/todos?userId={employee.get('id')}"
        todos = requests.get(endpoint).json()
        out_dict[employee.get("id")] = list(map(lambda x: {
            "username": employee.get("username"),
            "task": x.get("title"),
            "completed": x.get("completed")
        }, todos))
    with open(f"todo_all_employees.json", "w", newline="") as file:
        json.dump(out_dict, file)


if __name__ == "__main__":
    main()
