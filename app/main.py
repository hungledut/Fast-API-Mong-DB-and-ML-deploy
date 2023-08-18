"Main.py"
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from app.routes.users_routes import user_api_router
from app.routes.login_routes import login_api_router
from app.routes.iris_routes import iris_api_router
from app.logger.logger import custom_logger 

class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging All API request"""
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # start_time = time.time()
        # Log the request
        custom_logger.info("Received request: %s %s", request.method, request.url)
        # custom_logger.debug("Request headers: %s", request.headers)
        # custom_logger.debug("Request body: %s", await request.body())

        # Call the next middleware or route handler
        response = await call_next(request)
        # process_time = time.time() - start_time
        # response.headers['Process-Time'] = str(process_time)

        # Log the response
        custom_logger.info("Response status code: %s", response.status_code)
        # custom_logger.debug("Response headers: %s", response.headers)

        return response


app = FastAPI()

app.include_router(user_api_router)
app.include_router(login_api_router)
app.include_router(iris_api_router)
app.add_middleware(LoggingMiddleware)
