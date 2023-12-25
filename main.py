# main.py
from fastapi import FastAPI
from myfastapi.r_user import users_router


app = FastAPI()


@app.get("/")
async def root():
    return {"Hello World"}


app.include_router(users_router)
