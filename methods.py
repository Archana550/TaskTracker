
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"




def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file)

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        tasks = []
    print(tasks)
    return tasks




def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()

    if tasks:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1

    timestamp = datetime.now().isoformat()

    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {next_id})")


def update_task(task_id, new_description):
    tasks = load_tasks()

add_task("Learn Python")
add_task("Practice SQL")
