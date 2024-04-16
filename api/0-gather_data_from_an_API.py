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


def task_done(todo_list_data):
	completed_task = [task for task in todo_list_data if task["complete"]]
	return completed_task


def display_employee_info(user_data, completed_tasks, total_tasks):
	user_name = user_data["name"]
	len_completed_task = len(completed_tasks)

	print("Employee {} is done with tasks({}/{}):".format(

		user_name
		len_completed_task
		total_tasks))

	for task in completed_tasks:
		print(f"\t {task['title']}")

	if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python script.py <user_id>")
		sys.exit(1)

	user_id = sys.argv[1]

	user_info = get_user_info(user_id)
	todo_list = get_todo_list(user_id)
	completed_tasks = get_completed_tasks(todo_list)
	total_tasks = len(todo_list)

	display_employee_info(user_info, completed_tasks, total_tasks)
