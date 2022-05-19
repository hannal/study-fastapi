from fastapi import APIRouter

from . import controllers


__all__ = ["router"]

router = APIRouter()

router.get("/", name="hello:index")(controllers.hello)
