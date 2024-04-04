import secrets
import string
import hashlib
from saltmanager.SaltManager import create_salt, get_salt

secretSymbols = string.ascii_letters + string.digits      

def load_users() -> dict:
    #Here a file should be read to load existing users
    return {}

def generate_password() -> str:  
    return (''.join(secrets.choice(secretSymbols) for i in range(15)))

#Database would be way better ;)
users: dict = load_users()

class User:
    name: str
    password: str

    def __init__(self, name: str, password: str = ""):
        self.name = name
        salt = create_salt(name)    
        print("salt", salt)
        self.password = str(hashlib.sha256(password.join(salt).encode()).digest())

def get_user(username: str) -> User:
    return users.get(username)

def username_exists(username: str) -> bool:
    if not users.get(username) is None:
        return True
    return False

def create_user(username: str) -> User:
    if(username_exists(username=username)):
        return None
    password = generate_password()
    new_user = User(name=username, password=password)
    users[new_user.name] = new_user
    return (new_user, password)

def is_password_correct(username: str, password: str) -> bool:
    user = users.get(username)
    salt = get_salt(username=username)
    print("salt", salt)
    if user is None:
        return False 
    return user.password == str(hashlib.sha256(password.join(salt).encode()).digest())