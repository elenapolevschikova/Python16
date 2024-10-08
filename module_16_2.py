from fastapi import FastAPI, Path   # Установили фреймворк FastAPI при помощи пакетного менеджера pip.
from typing import Annotated

app = FastAPI()    # Создали приложение(объект) FastAPI предварительно импортировав класс для него.


@app.get("/")    # Создайли маршрут к главной странице - "/".
async def get_main_page() -> dict:
    return {"user": "Главная страница"}   # По нему должно выводиться сообщение "Главная страница".


@app.get("/user")   # Создали маршрут к страницам пользователей передавая данные в адресной строке - "/user".
async def get_user_info() -> dict:
    return {"user": f"Информация о пользователе "}
    # По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".



@app.get("/user/{user_id}")  # Создали маршрут к страницам поль-й ис-я параметр в пути - "/user/{user_id}
async def get_user_number(user_id: int) -> dict:
    return {"user": f"Вы вошли как пользователь № {user_id}"}
    # По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".


@app.get("/user/{user_id}")  # если мы получили .get("/")-гет запрос
async def get_main_page(user_id: Annotated[int, Path(ge=5, le=20, description="Enter User ID", example="1")]) -> dict:
    # Path - проверяет какой тип данных приходит,и хранит их
    return {"message": f"Hello, {user_id}"}


@app.get("/user/{username}/{age}")  # если мы получили .get("/")-гет запрос
async def get_main_page(username: Annotated[str, Path(min_length=5, max_length=20
    , description="Enter username", example="UrbanUser")]
               , age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    # Path - проверяет какой тип данных приходит и хранит их, Annotated - помогает работать с большестроками
    return {"user": f"Hello, {username} {age}"}


# @app.get("/id")
# async def id_paginator(username: str = 'Alex', age: int = 34) -> dict:  # передаём по умолчанию
#     return {"User": username, "Age": age}
