from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_dev():
    return "Hello world"


@app.get("/get_id/{pk}")
async def get_my_id(pk: int):
    return {"pk": pk}


@app.get("/kvadrat/{number}")
async def kvadrat(number: int):
    return {'number': number ** 2}


@app.get("/kub/{number}")
async def kub(number: int):
    return {'number': number ** 3}
