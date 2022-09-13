from pydantic import BaseModel
from bson.objectid import ObjectId


class PersonModel(BaseModel):
	_id: ObjectId
	name: str
	age: int | None
	height: float | None


class UpdatePersonDTO(BaseModel):
	id: str
	name: str
	age: int | None
	height: float | None


class PersonDTO(BaseModel):
	name: str
	age: int | None
	height: float | None
