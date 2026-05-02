import json
from datetime import datetime
import uuid

filename = 'data.json'

class Task:
    def add(self, description, status):
        self.description = description
        self.status = status

        try:
            with open(filename, 'r') as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        data = {
                'id': str(uuid.uuid4()),
                'description': self.description,
                'status': self.status,
                'createdAt': str(datetime.now()),
                'updatedAt': str(datetime.now())
        }
        tasks.append(data)

        with open(filename, "w")as file:
            json.dump(tasks, file, indent=4)

        return (f"Task added successfuly (ID: {data['id']})")
    
    def update(self, task_id, new_description=None, new_status=None):
        try:
            with open(filename, 'r')as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return "No tasks found"
        
        found = False

        for task in tasks:
            if task["id"] == task_id:
                if new_description:
                    task['description'] = new_description
                if new_status:
                    task["status"] = new_status

                task["updatedAt"] = datetime.now().isoformat()
                found = True
                break

        if not found:
            return f"Task with ID {task_id} not found."
        
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)

        return f"Tasks {task_id} updated successfully"

    def delete(self, task_id):
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return "No tasks"
        
        data = []

        for task in tasks:
            if task["id"] != task_id:
                data.append(task)

        with open(filename, "w")as file:
            json.dump(data, file, indent=4)

        return f'Item {task_id} successfully deleted.'
    
    def list(self, filter=None):
        with open(filename, "r")as file:
            tasks = json.load(file)

        data = []
        for task in tasks:
            if filter == 'Done':
                if task['status'] == 'Done':
                    data.append(task)
            elif filter == 'Todo':
                if task['status'] == 'Todo':
                    data.append(task)
            elif filter == 'In-progress':
                if task['status'] == 'In-progress':
                    data.append(task)
            else:
                data.append(task)

        
        return data


task = Task()

print(task.list())