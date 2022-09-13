from typing import Any

from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from person_schemas import PersonDTO, UpdatePersonDTO, PersonModel
import person_service

app = FastAPI()


@app.get("/person/", response_model=list[PersonDTO])
def get_all():
	person_list: list[PersonDTO] = person_service.find_all()
	return JSONResponse(content=to_json(person_list), status_code=200)


@app.get("/person/{person_id}")
def get_by_id(person_id: str):
	# person: PersonModel | None = person_DAO.find_person_by_id(person_id)
	pass
	# return Response(content=person, status_code=200)


@app.post("/person/")
def create_person(person: PersonDTO):
	# person_DAO.save_person(person)
	return Response(status_code=201)


@app.put("/person/")
def update_person(person: UpdatePersonDTO):
	pass


@app.delete("/person/")
def delete_person(person: PersonDTO):
	pass
	return Response(status_code=200)


def to_json(obj: Any):
	return jsonable_encoder(obj)
