import secrets
import json
import string

def load_users() -> dict:
    #Here a file should be read to load existing users
    return {}

def generate_password() -> str:
    symbols = string.ascii_letters.join(string.digits)        
    return (''.join(secrets.choice(symbols) for i in range(15)))

users: dict = load_users()

class User:
    name: str
    password: str

    def __init__(self, name: str, password: str = ""):
        self.name = name
        if password == "":
            self.password = generate_password()
        else:
            self.password = password

def get_user(username: str) -> User:
    return users.get(username)

def username_exists(username: str) -> bool:
    if not users.get(username) is None:
        return True
    return False

def create_user(username: str) -> User:
    if(username_exists(username=username)):
        return None
    new_user = User(name=username)
    users[new_user.name] = new_user
    return new_user

def is_password_correct(username: str, password: str) -> bool:
    user = users.get(username)
    if user is None:
        return False 
    return user.password == password