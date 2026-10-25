import sys
import methods

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python cli.py <command> [arguments]")
        return


    command = args[0]

    if command == "add":
        if len(args) != 2:
            print('Usage: python cli.py and "description"')
            return

        methods.add_task(args[1])

    elif command == "update":
        if len(args) != 3:
            print('Usage: python cli.py update <id> "new description"')
            return

        try:
            task_id = int(args[1])
        except ValueError:
            print("Task ID must be a number.")
            return

        methods.update_task(task_id,args[2])

    elif command == "delete":
        if len(args) != 2:
            print("Usage : python cli.py delete <id>")
            return

        try:
            task_id = int(args[1])
        except ValueError:
            print("Task ID must be a number.")
            return

        if methods.delete_task(task_id):
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task not found (ID: {task_id})")

    elif command == "mark-in-progress":
        if len(args) != 2:
            print("Usage: python cli.py mark-in-progress <id>")
            return
        try:
            task_id = int(args[1])
        except ValueError:
            print("Task ID must be a number.")
            return

        methods.mark_task(task_id, "in-progress")

    elif command == "mark-done":
        if len(args)!= 2:
            print("Usage: python cli.py mark-done <id>")
            return
        try:
            task_id = int(args[1])
        except ValueError:
            print("Task ID must be a number.")
            return
        methods.mark_task(task_id, "done")


    elif command == "list":
        if len(args)>2:
            print("Usage : python cli.py list[to|done|in progress]")
            return

        status = args[1] if len(args) ==2 else None

        if status == "not-done":
            status = "todo"

        if status not in (None, "todo", "done","in-progress"):
            print("Invalid status . Use todo, done, or in progress.")
            return

        methods.list_tasks(status)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

