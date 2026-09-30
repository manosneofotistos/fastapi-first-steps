from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="First API")

class GreetingInput(BaseModel):
    name: str

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.post("/greet")
def greet(body: GreetingInput):
    return {"message": f"Hello, {body.name}!"}