#!/usr/bin/python3
"""Export to JSON"""

import json
import sys
import requests


if __name__ == "__main__":
    # field names
    fields = { "USER_ID": [{"task": "TASK_TITLE", "completed":
              "TASK_COMPLETED_STATUS", "username": "USERNAME"},
              {"task": "TASK_TITLE",
              "completed": "TASK_COMPLETED_STATUS", "username": "USERNAME"}]}

    employee_id = sys.argv[1]

    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(api_url)
    username = response.json()['username']

    # data of json file
    api_url1 = (f"https://jsonplaceholder.typicode.com"
                f"/todos?userId={employee_id}")
    new_response = requests.get(api_url1)
    data = new_response.json()
    # name of json file
    filename = f"{employee_id}.json"

    # write to json file
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
