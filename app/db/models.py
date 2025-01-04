from datetime import datetime
from typing import Optional
from pymongo import IndexModel, ASCENDING
from pymongo.collection import Collection
from app.db.database import get_collection
from bson import ObjectId


class UserModel:
    collection: Collection = get_collection("users")

    # Create indexes
    collection.create_indexes([IndexModel([("username", ASCENDING)], unique=True)])

    @staticmethod
    async def create_user(username: str, hashed_password: str, role: str) -> dict:
        user = {
            "username": username,
            "hashed_password": hashed_password,
            "role": role,
            "created_at": datetime.utcnow(),
        }
        result = await UserModel.collection.insert_one(user)
        return user

    @staticmethod
    async def get_user(username: str) -> Optional[dict]:
        return await UserModel.collection.find_one({"username": username})


class ProjectModel:
    collection: Collection = get_collection("projects")

    @staticmethod
    async def create_project(name: str, description: str, created_by: str) -> dict:
        project = {
            "name": name,
            "description": description,
            "created_by": created_by,
            "created_at": datetime.utcnow(),
        }
        result = await ProjectModel.collection.insert_one(project)
        project["id"] = str(result.inserted_id)
        return project

    @staticmethod
    async def get_projects() -> list:
        cursor = ProjectModel.collection.find({})
        projects = await cursor.to_list(length=None)
        for project in projects:
            project["id"] = str(project.pop("_id"))
        return projects

    @staticmethod
    async def get_project(project_id: str) -> Optional[dict]:
        project = await ProjectModel.collection.find_one({"_id": ObjectId(project_id)})
        if project:
            project["id"] = str(project.pop("_id"))
        return project

    @staticmethod
    async def delete_project(project_id: str) -> bool:
        result = await ProjectModel.collection.delete_one({"_id": ObjectId(project_id)})
        return result.deleted_count > 0
