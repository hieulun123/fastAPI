# user_router
from typing import List
from uuid import uuid4
from fastapi import APIRouter
from myfastapi.models import Gender, Role, User, UpdateUser
from uuid import UUID
from fastapi import HTTPException


users_router = APIRouter()


db: List[User] = [
    User(
        id=uuid4(),
        first_name="hieu",
        last_name="vu",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="minh",
        last_name="tran",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="tham",
        last_name="hoang",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(

        id=uuid4(),
        first_name="nam",
        last_name="tran",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


@users_router.get("/users/")
async def get_users():
    return db


@users_router.post("/users/")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@users_router.delete("/users/{id}/")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return user.id
    raise HTTPException(
            status_code=404, detail=f"Delete user failed, id {id} not found."
        )


@users_router.put("/users/{id}/")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
    raise HTTPException(status_code=404,
                        detail=f"Could not find user with id: {id}")
