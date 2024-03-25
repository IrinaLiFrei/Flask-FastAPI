# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

import sqlalchemy
import uvicorn
from fastapi import FastAPI
import databases
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import date

DATABASE_URL = 'sqlite:///hw6.db'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(64)),
    sqlalchemy.Column('last_name', sqlalchemy.String(64)),
    sqlalchemy.Column('date_of_birth', sqlalchemy.Date),
    sqlalchemy.Column('email', sqlalchemy.String(32)),
    sqlalchemy.Column('address', sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    first_name: str = Field(title='First Name', min_length=2)
    last_name: str = Field(title='First Name', min_length=2)
    date_of_birth: date = Field(title='Date Of Birth')
    email: EmailStr = Field(title='Email', max_length=128)
    address: str = Field(title='Address', min_length=5)


class User(UserIn):
    id: int = Field(title='ID')



@app.post('/users/', response_model=User)
async def add_user(user: UserIn):
    query = users.insert().values(first_name=user.first_name, last_name=user.last_name,
                                      date_of_birth=user.date_of_birth, email=user.email, address=user.address)
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}


@app.get('/temp/{number}')
async def temp_user(number: int):
    for i in range(number):
        query = users.insert().values(first_name=f'First_name_{i + 1}',
                                      last_name=f'Last_name_{i + 1}',
                                      date_of_birth=date.today(),
                                      email=f'user{i + 1}@mail.com',
                                      address=f'{i + 1}' * 8)
        await database.execute(query)
    return 'OK'


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}/', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put('/users/{user_id}/', response_model=User)
async def update_user(user_id: int, updated_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(first_name=updated_user.first_name, last_name=updated_user.last_name,
                                      date_of_birth=updated_user.date_of_birth, email=updated_user.email, address=updated_user.address)
    last_record_id = await database.execute(query)
    await database.execute(query)
    return {**updated_user.dict(), 'id': last_record_id}


@app.delete('/users/{user_id}/')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
