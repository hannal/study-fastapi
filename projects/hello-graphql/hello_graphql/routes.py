from fastapi import APIRouter

from hello_graphql.graphql import router as graphql_router
from apps.hello.routes import router as hello_router


router = APIRouter()

router.include_router(hello_router, prefix="/hello")

router.include_router(graphql_router, prefix="/graphql")
router.add_websocket_route("/graphql", graphql_router)
