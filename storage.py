import json
import os

STORAGE_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(STORAGE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)