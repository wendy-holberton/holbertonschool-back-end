#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    # field names
    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    employee_id = sys.argv[1]

    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(api_url)
    username = response.json()['username']

    # data of csv file
    api_url1 = (f"https://jsonplaceholder.typicode.com"
                f"/todos?userId={employee_id}")
    new_response = requests.get(api_url1)
    data = new_response.json()
    # name of csv file
    filename = f"{employee_id}.csv"

    # write to csv file
    with open(filename, 'w', newline='') as file:
        # create a csv writer object
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for r in data:
            row = [r['userId'], username, r['completed'], r['title']]
            csv_writer.writerow(row)
