# task_manager.py

import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, title, description=""):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {title}")
    
    def list_tasks(self, show_completed=True):
        """List all tasks"""
        if not self.tasks:
            print("📭 No tasks found!")
            return
        
        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
            
            status = "✓" if task["completed"] else "□"
            print(f"{status} [{task['id']}] {task['title']}")
            if task['description']:
                print(f"   📝 {task['description']}")
            print(f"   📅 {task['created_at']}")
            print()
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"🎉 Task completed: {task['title']}")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"🗑️  Task deleted: {deleted_task['title']}")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        
        print("\n📊 Task Statistics:")
        print(f"   Total tasks: {total}")
        print(f"   Completed: {completed}")
        print(f"   Pending: {pending}")
        if total > 0:
            print(f"   Progress: {(completed/total)*100:.1f}%")

def main():
    manager = TaskManager()
    
    while True:
        print("\n" + "="*50)
        print("📋 TASK MANAGER")
        print("="*50)
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Pending Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. View Statistics")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            title = input("Task title: ").strip()
            if not title:
                print("❌ Title cannot be empty!")
                continue
            description = input("Description (optional): ").strip()
            manager.add_task(title, description)
        
        elif choice == "2":
            print("\n📋 ALL TASKS:")
            print("-" * 40)
            manager.list_tasks(show_completed=True)
        
        elif choice == "3":
            print("\n📋 PENDING TASKS:")
            print("-" * 40)
            manager.list_tasks(show_completed=False)
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        elif choice == "6":
            manager.get_statistics()
        
        elif choice == "7":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-7")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()