from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
	name: str
	age: int | None = None


@app.get("/{path}")
def get_root(path: str, q: str | None = None):
	print(q)
	return {"message": "Hello World!", "path": path}


@app.post("/")
def post_root(person: Person):
	return person

