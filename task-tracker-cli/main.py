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
        

task = Task()

print(task.update("5e29eeae-2805-471b-8c22-0b82c0c6e51c", None, "Done"))