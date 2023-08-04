from fastapi import FastAPI, HTTPException,Depends,APIRouter
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Union, Any
import jwt
from security import reusable_oauth2
from models.user_model import User
from config.database import collection_name

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

login_api_router = APIRouter()


#Hàm check username và password từ database
def verify_password(username, password):
    user = collection_name.find_one({"username": username})
    if user == None or password != user['password']:
        return False
    return True

def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt

#Hàm login 
@login_api_router.post('/')
async def login(request_data: User):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")