from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI(
    title="My First fats-api Test urls",
    description="## This is my first testing **deploy**",
    docs_url='/swagger',
)


@app.get("/")
async def main_dev():
    return "Hello world"


@app.get("/get_id/{pk}")
async def get_my_id(pk: int):
    return {"pk": pk}


@app.get("/kvadrat/{number}")
async def kvadrat(number: int):
    return {'kvadrat': number ** 2}


@app.get("/kub/{number}")
async def kub(number: int):
    return {'kub': number ** 3}


@app.get("/yigindi")
async def yigindi(items: Annotated[list[int], Query()]):
    return {'yigindi': sum(items)}


@app.get("/ayirma")
async def ayirma(a: int, b: int):
    return {'ayirma': a - b}


@app.get("/kopaytma")
async def kopaytma(a: int, b: int):
    return {'kopaytma': a * b}


@app.get("/bolinma")
async def bolinma(a, b):
    pass
