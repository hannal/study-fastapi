from fastapi import APIRouter

from apps.hello.routes import router as hello_router


router = APIRouter()

router.include_router(hello_router, prefix="/hello")
