from fastapi import FastAPI
from usermanager.UserManager import *
from model.Login import Login

app = FastAPI()

@app.post("/user/{username}")
async def root(username: str):
    new_user = create_user(username=username)
    if new_user is None:
        return "user could not be created"
    else:
        return new_user
    
@app.get("/user/{username}")
async def does_user_exist(username: str):
    print("check if username exists")
    return username_exists(username=username)
    
@app.get("/login/{username}")
async def check_if_password_is_correct(username: str, login: Login):
    print("check if passsword correct")
    return is_password_correct(username=username, password=login.password)