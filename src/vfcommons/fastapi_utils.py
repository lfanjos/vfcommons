from fastapi import HTTPException, FastAPI
from fastapi.responses import JSONResponse

async def custom_http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "message": "Error",
            "data": exc.detail
        },
    )


def configure_exception_handlers(app: FastAPI):
    app.add_exception_handler(HTTPException, custom_http_exception_handler)
