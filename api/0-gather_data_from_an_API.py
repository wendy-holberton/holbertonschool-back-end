#!/usr/bin/python3
"""
Gather data from API
"""

import requests
import sys


def employee_todo_list(employee_id):
    """define employee_todo_list function passing argument employee_id"""

    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(api_url)
    employee_name = response.json()['name']

    api_url1 = f"https://jsonplaceholder.typicode.com"
    "/todos?userId={employee_id}"
    new_response = requests.get(api_url1)
    total_number_of_tasks = len(new_response.json())

    number_of_done_tasks = 0
    completed_title = 0

    completed_title = []

    for item in new_response.json():
        if item['completed'] is True:
            number_of_done_tasks = number_of_done_tasks + 1
            completed_title.append(item['title'])

    print(f"Employee {employee_name} is done with tasks"
          "({number_of_done_tasks}/{total_number_of_tasks}):")
    for title in completed_title:
        print(f"\t {title}")


employee_todo_list(sys.argv[1])
