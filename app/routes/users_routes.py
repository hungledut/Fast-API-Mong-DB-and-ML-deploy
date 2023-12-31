"User Routes"
from fastapi import APIRouter,Depends
from bson import ObjectId

from app.models.user_model import User
from app.config.database import collection_name
from app.security import validate_token
from app.schemas.user_schema import users_serializer

user_api_router = APIRouter(tags = ['User'])

# retrieve
@user_api_router.get("/",dependencies=[Depends(validate_token)])
async def get_users():
    "Get all users"
    users = users_serializer(collection_name.find())
    return users

@user_api_router.get("/{id}",dependencies=[Depends(validate_token)])
async def get_user(user_id: str):
    "Get each user with id"
    return users_serializer(collection_name.find_one({"_id": ObjectId(user_id)}))


#post
@user_api_router.post("/create",dependencies=[Depends(validate_token)])
async def create_user(user: User):
    "Create a user"
    _id = collection_name.insert_one(dict(user))
    return users_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@user_api_router.put("/update/{user_id}",dependencies=[Depends(validate_token)])
async def update_user(user_id: str, user: User):
    "Update a user"
    collection_name.find_one_and_update({"_id": ObjectId(user_id)}, {
        "$set": dict(user)
    })
    return users_serializer(collection_name.find({"_id": ObjectId(user_id)}))

# delete
@user_api_router.delete("/delete/{user_id}",dependencies=[Depends(validate_token)])
async def delete_user(user_id: str):
    "Delete a user"
    collection_name.find_one_and_delete({"_id": ObjectId(user_id)})
    return {"status": "ok"}
