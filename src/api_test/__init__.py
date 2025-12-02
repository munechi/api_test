from fastapi import FastAPI


app = FastAPI()


@app.get("/add/{a}/{b}")
def add(a: int, b: int) -> int:
    return int(a) + int(b)


@app.get("/sub/{a}/{b}")
def sub(a: int, b: int) -> int:
    return int(a) - int(b)


@app.get("/mul/{a}/{b}")
def sub(a: int, b: int) -> int:
    return int(a) * int(b)
