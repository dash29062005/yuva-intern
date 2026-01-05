import argparse
from todo.task_manager import TaskManager
from todo import storage
from security.logger import log_error


def main():
    parser = argparse.ArgumentParser(
        description="CLI To-Do Task Manager"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---------------- ADD ----------------
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str)
    add_parser.add_argument("-p", "--priority", choices=["low", "mid", "high"], default="mid")
    add_parser.add_argument("-d", "--duration", type=str)

    # ---------------- UPDATE ----------------
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("-t", "--title", type=str)
    update_parser.add_argument("-p", "--priority", choices=["low", "mid", "high"])
    update_parser.add_argument("-d", "--duration", type=str)

    # ---------------- DELETE ----------------
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int)

    # ---------------- COMPLETE ----------------
    complete_parser = subparsers.add_parser("complete", help="Mark task completed")
    complete_parser.add_argument("id", type=int)

    # ---------------- LIST ----------------
    list_parser = subparsers.add_parser("list", help="List tasks")
    group = list_parser.add_mutually_exclusive_group()
    group.add_argument("--completed", action="store_true")
    group.add_argument("--pending", action="store_true")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        # Load tasks
        raw_tasks = storage.load_tasks()
        manager = TaskManager(raw_tasks)

        # Execute command
        if args.command == "add":
            task = manager.add_task(args.title, args.priority, args.duration)
            print(f"Added task [{task.id}] {task.title}")

        elif args.command == "update":
            task = manager.update_task(args.id, args.title, args.priority, args.duration)
            print(f"Updated task [{task.id}]")

        elif args.command == "delete":
            manager.delete_task(args.id)
            print(f"Deleted task [{args.id}]")

        elif args.command == "complete":
            task = manager.complete_task(args.id)
            print(f"Completed task [{task.id}]")

        elif args.command == "list":
            status = "completed" if args.completed else "pending" if args.pending else None
            tasks = manager.list_tasks(status)

            if not tasks:
                print("No tasks found.")
                return

            print(f"Total tasks: {len(tasks)}")

        # Save changes
        if args.command != "list":
            storage.save_tasks(manager.to_dict())

    except Exception as e:
        log_error(str(e))
        print("An error occurred. Please check your input or try again.")


if __name__ == "__main__":
    main()
