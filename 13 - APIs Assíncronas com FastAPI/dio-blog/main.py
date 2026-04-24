from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_():
    return {"message": "Hello Word"}