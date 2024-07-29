tasks = []

def add_task(description):
 """Add a new task"""
 task = {
  "id": len(tasks) + 1,
  "description": description, 
  "completed":False
 }
 tasks.append(task)
 print(f"Task added: {description}")


def read_task():
 "Read the list of tasks"
 if not tasks:
  print("No tasks found!")
  return 
 for task in tasks:
  status = "✔️" if task['completed'] else "❌"
  print(f"{task['id']}. {task['description']} [{status}]")


def update_task(task_id, new_description):
 """Update the existing tasks"""
 for task in tasks:
  if task["id"] == task_id:
   task["description"] = new_description
   print(f"Task{task_id}, updated to: {new_description}")
   return
 print(f"Task {task_id} not found.")


def delete_task(task_id):
 global tasks 
 tasks = [task for task in tasks if task["id"] != task_id]
 print(f"Task {task_id} deleted. ")


def complete_task(task_id):
 "Check the status of a task"
 for task in tasks:
  if task["id"] == task_id:
   task["completed"] = True
   print(f"Task {task_id} marked as completed.")
   return 
  print(f"Task {task_id} not found.")
