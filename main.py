from turtle import title
from fastapi import FastAPI

app = FastAPI(title='Holap', version='0.0.1', description='Holap API')


@app.get("/")
def hello_world():
    return {"message": "Hello World"}