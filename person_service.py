from bson.objectid import ObjectId

import person_DAO
import person_mapper
from person_schemas import PersonDTO, PersonModel, UpdatePersonDTO


def find_all() -> list[PersonDTO]:
	person_model_list: list[PersonModel] = person_DAO.find_all()
	return person_mapper.person_model_list_to_dto_list(person_model_list)


def find_person_by_id(person_id: str) -> PersonDTO:
	person_object_id: ObjectId = person_mapper.__str_to_object_id(person_id)
	person_model: PersonModel | None = person_DAO.find_person_by_id(person_object_id)
	person_to_return: PersonDTO = person_mapper.person_model_to_dto(person_model)
	if person_to_return is None:
		raise ValueError

	return person_to_return


def update_person_by_id(update_person_dto: UpdatePersonDTO) -> PersonDTO:
	person_model: PersonModel = person_mapper.update_person_dto_to_model(update_person_dto)
	person_to_return: PersonDTO = person_mapper.person_model_to_dto(person_DAO.update_person_by_id(person_model))
	if person_to_return is None:
		raise ValueError

	return person_to_return
