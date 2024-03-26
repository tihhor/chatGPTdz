from fastapi import FastAPI
from pydantic import BaseModel

# аннотации типов
# класс с типами данных параметров
class Item(BaseModel):
    num1: float
    num2: float

# создаем объект приложения
app = FastAPI()

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:5000/
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


# функция-обработчик post запроса с параметрами
@app.post("/plus")
def plus(item:Item):
    result = item.num1 + item.num2
    return {"result": result}

# функция-обработчик post запроса с параметрами
@app.post("/minus")
def minus(item:Item):
    result = item.num1 - item.num2
    return {"result": result}

# функция-обработчик post запроса с параметрами
@app.post("/mult")
def mult(item:Item):
    result = item.num1 * item.num2
    return {"result": result}

# функция-обработчик post запроса с параметрами
@app.post("/divide")
def divide(item:Item):
    if item.num2 == 0:
        result = ('Нельзя делить на ноль!')
    else:
        result = item.num1 / item.num2
    return {"result": result}


# проверка запросов

import requests

# проверочные запросы в fastapi
# response = requests.get("http://127.0.0.1:5000/")
# print(response.text)

data={"num1": 100, "num2": 12.50}

response = requests.post("http://127.0.0.1:5000/plus", json=data)
print('Сложение:', response.text)

response = requests.post("http://127.0.0.1:5000/minus", json=data)
print('Вычитание:', response.text)

response = requests.post("http://127.0.0.1:5000/mult", json=data)
print('Умножение:', response.text)

response = requests.post("http://127.0.0.1:5000/divide", json=data)
print('Деление:', response.text)
