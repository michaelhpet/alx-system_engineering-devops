#!/usr/bin/python3
"""Gather data from an API."""
import json
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
    with open(f"{user_id}.json", "w", newline="") as file:
        out_dict = {}
        out_dict[user_id] = list(map(lambda x: {
            "username": employee.get("username"),
            "task": x.get("title"),
            "completed": x.get("completed")
        }, todos))
        json.dump(out_dict, file)


if __name__ == "__main__":
    main()
