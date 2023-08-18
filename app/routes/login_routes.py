"Login Routes"

from typing import Union, Any
from datetime import datetime, timedelta
from fastapi import APIRouter,HTTPException

import jwt
from app.models.user_model import User
from app.config.database import collection_name

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

login_api_router = APIRouter(tags = ['Login'])



def verify_password(username, password):
    "Check user and password from database"
    user = collection_name.find_one({"username": username})
    if user is None or password != user['password']:
        return False
    return True

def generate_token(username: Union[str, Any]) -> str:
    "This function to generate a token"
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt


@login_api_router.post('/')
async def login(request_data: User):
    "Login with username and password"
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")
