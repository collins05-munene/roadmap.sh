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
    

task = Task()
print(task.add("Learn Django", "Todo"))