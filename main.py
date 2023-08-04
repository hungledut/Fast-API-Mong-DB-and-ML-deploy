from fastapi import FastAPI
from routes.users_routes import user_api_router
from routes.login_routes import login_api_router

app = FastAPI()

app.include_router(user_api_router)
app.include_router(login_api_router)