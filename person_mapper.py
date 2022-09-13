from bson import ObjectId
from bson.errors import InvalidId

from person_schemas import PersonDTO, PersonModel, UpdatePersonDTO


def person_model_to_dto(person_model: PersonModel) -> PersonDTO | None:
	if person_model is None:
		return None

	return PersonDTO.parse_obj(person_model.dict())


def person_model_list_to_dto_list(person_model_list: list[PersonModel]) -> list[PersonDTO]:
	person_dto_list: list[PersonDTO] = []

	for person_model in person_model_list:
		person_dto_list.append(person_model_to_dto(person_model))

	return person_dto_list


def update_person_dto_to_model(update_person_dto: UpdatePersonDTO) -> PersonModel | None:
	if update_person_dto is None:
		return None

	_id: ObjectId = __str_to_object_id(update_person_dto.id)
	name: str = update_person_dto.name
	age: int = update_person_dto.age
	height: float = update_person_dto.height

	return PersonModel(_id=_id, name=name, age=age, height=height)


def __str_to_object_id(str_id: str):
	try:
		return ObjectId(str_id)
	except (InvalidId, ValueError):
		raise ValueError("Invalid ObjectId")
