#!/usr/bin/python3
"""Export to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    # field names
    fields = {"USER_ID": [{"task": "TASK_TITLE", "completed":
"TASK_COMPLETED_STATUS", "username": "USERNAME"}]}
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

    for item in data:
        item["task"] = item.pop("title")
        del item["userId"]
        del item["id"]
        item["username"] = username

    new_data = {employee_id: data}

    json_str = json.dumps(new_data)

    with open(filename, 'w') as jfile:
        jfile.write(json_str)
