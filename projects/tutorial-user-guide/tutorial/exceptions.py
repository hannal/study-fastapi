from fastapi import status, HTTPException


class BaseHttpTeapotError(HTTPException):
    status_code = status.HTTP_418_IM_A_TEAPOT
    detail = "teapot teapot error"

    def __init__(self, /, **kwargs):
        kwargs.pop("status_code", None)
        detail = kwargs.pop("detail", self.detail)
        super().__init__(status_code=self.status_code, detail=detail, **kwargs)
