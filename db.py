import json
import os

file_name = 'users.json'
if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        json.dump({}, f)


def get_users() -> dict:
    with open(file_name) as f:
        return json.load(f)
    return {}

def save_users(users: dict):
    with open(file_name, 'w') as f:
        json.dump(users, f, indent=4)

def add_user(tg_id: int, full_name: str, username: str | None = None):
    users = get_users()

    if str(tg_id) not in users:
        users[str(tg_id)] = {
            'full_name': full_name,
            'username': username
        }

        save_users(users)
        return True
    
    return False
