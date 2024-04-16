#!/usr/bin/python3
"""Script that display infos for a given employee"""

import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def get_user_info(user_id):
    user_request = requests.get(f"{API_URL}/users/{user_id}")
    user_data = user_request.json()
    return user_data


def get_todo_list(user_id):
    todo_list = requests.get(f"{API_URL}/todo?userID={user_id}")
    todo_list_data = todo_list.json()
    return todo_list_data
