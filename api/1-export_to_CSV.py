#!/usr/bin/python3
""" Script that exports data in the CSV format """

import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":

    employee_id = sys.argv[1]
