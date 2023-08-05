"User Model"
from pydantic import BaseModel


class User(BaseModel):
    "User schema"
    username : str
    password : str
