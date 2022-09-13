from pymongo import MongoClient
from pymongo.results import InsertOneResult, UpdateResult
from pymongo.database import Database, Collection
from bson.objectid import ObjectId

from person_schemas import PersonModel

client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["db_test_python"]

collection_name: str = "person"
collection: Collection
if collection_name not in db.list_collection_names():
	collection = db.create_collection(collection_name)
else:
	collection = db.get_collection(collection_name)


def save_person(person: PersonModel) -> ObjectId:
	result: InsertOneResult = collection.insert_one(person.dict())
	return result.inserted_id


def find_all() -> list[PersonModel]:
	person_list: list[PersonModel] = []

	for person in collection.find():
		person_list.append(person)

	return person_list


def find_person_by_id(person_id: ObjectId) -> PersonModel | None:
	return PersonModel.parse_obj(collection.find({"_id": person_id}).next())


def update_person_by_id(person_model: PersonModel) -> PersonModel:
	result: UpdateResult = collection.update_one({"_id": person_model.dict()["_id"]}, person_model.dict())
	return PersonModel.parse_obj(result.raw_result)


def delete_person_by_id(person_id: ObjectId) -> None:
	collection.delete_one({"_id": person_id})
