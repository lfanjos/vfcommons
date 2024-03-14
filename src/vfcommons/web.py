from fastapi import HTTPException
import inspect

class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str, path: str = None):
        if path is None:
            caller_frame = inspect.stack()[1]
            path = f'{caller_frame.filename} -> {caller_frame.function}'

        super().__init__(status_code=status_code, detail={
            "detail": detail,
            "path": path
        })