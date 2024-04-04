import secrets
import string

def load_salts():
    return {}

#Database would be way better ;)
salts: dict= load_salts()
secretSymbols = string.ascii_letters + string.digits

def create_salt(username: str) -> str:
    salt = ''.join(secrets.choice(secretSymbols) for i in range(10))
    print("created salt", str(salt))
    salts[username] = salt
    return salt

def get_salt(username: str) -> str:
    return salts.get(username)