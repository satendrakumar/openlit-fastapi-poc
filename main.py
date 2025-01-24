import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse


from src.api.chat_api import chat_api
from src.util.logger import get_logger
import openlit

openlit.init(application_name="chat_app")

log = get_logger(__name__)

APP_PORT = int(os.getenv("APP_PORT", default=8000))

app = FastAPI()

app.include_router(chat_api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = await request.json()
    log.error(f"Request Validation Error: {exc.errors()} \n Body: {body}")
    return JSONResponse(
        status_code=422,
        content={"error": exc.errors()},
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=False,
        port=APP_PORT
    )