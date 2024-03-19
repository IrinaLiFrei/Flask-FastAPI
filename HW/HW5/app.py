
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='./templates')


class User(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_pwd: str


users = []
for i in range(5):
    id = i + 1
    name = "name_" + str(i+1)
    email = name + str(id) + '@' + str(i+1) + '.com'
    pwd = str(i+1) * 3
    user = User(user_id=id, user_name=name, user_email=email, user_pwd=pwd)
    users.append(user)
print(users)


@app.get('/')
async def read_root():
    return 'Hello World!'


@app.get('/users/', response_class=HTMLResponse)
async def get_html(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.post("/users/{user_id}")
async def create_user(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(u_id: int, user: User):
    for i in range(len(users)):
        if users[i].user_id == u_id:
            users[i] = user
    return {"user_id": u_id, "user": user}


@app.delete("/users/{user_id}")
async def delete_user(u_id: int):
    for u in users:
        if u.user_id == u_id:
            users.remove(u)
    return {"user_id": u_id}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)

