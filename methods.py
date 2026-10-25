
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

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return True

    print(f"Task not found (ID:{task_id})")
    return False       


def list_tasks(status=None):
    tasks = load_tasks()

    filtered_tasks = [
        task for task in tasks
        if status is None or task["status"] == status
    ]

    if not filtered_tasks:
        print("No tasks found.")
        return

    for task in filtered_tasks:
        print(
            f'ID: {task["id"]} | '
            f'Description: {task["description"]} | '
            f'Status: {task["status"]} | '
            f'Created: {task["createdAt"]} | '
            f'Updated: {task["updatedAt"]}'
        )
 

def delete_task(task_id):
   tasks = load_tasks()
  
   remaining_tasks = [
       task for task in tasks
       if task["id"]!= task_id
   ]

   if len(remaining_tasks) == len(tasks):
       return False
   
   save_tasks(remaining_tasks)
   return True
               

def mark_task(task_id, status):
    if status not in ("in-progress", "done"):
        print("Invalid status. Use 'in-progress' or 'done")
        return False
    tasks = load_tasks()

    for task in tasks:
        if task["id"] ==task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return True
    print(f"Task not found (ID:{task_id})")
    return False



