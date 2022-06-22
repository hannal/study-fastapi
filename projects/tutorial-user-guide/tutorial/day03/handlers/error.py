from fastapi import status, Request, HTTPException
from fastapi.responses import JSONResponse

from ...exceptions import BaseHttpTeapotError
from ..app import app


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "message": f"Oops! {exc.detail}. There goes a rainbow...",
            "custom_field": "not-found",
        },
    )


class Day03CustomError(BaseHttpTeapotError):
    detail = "day03-teapot-error"


async def teapot_error_handler(request: Request, exc: BaseHttpTeapotError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "custom_field": "teapot!",
        },
    )


app.add_exception_handler(BaseHttpTeapotError, teapot_error_handler)
