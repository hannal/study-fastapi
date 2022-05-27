import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import Depends

from apps.hello.models.schemas import User, get_user
from apps.hello.models.schemas import create_user


__all__ = [
    "Query",
    "Mutation",
    "schema",
    "router",
]


def custom_context_dependency() -> str:
    return "John"


async def get_context(custom_value=Depends(custom_context_dependency)):
    return {
        "custom_value": custom_value,
    }


@strawberry.type
class Query:
    user: User = strawberry.field(get_user)


@strawberry.type
class Mutation:
    create_user = strawberry.mutation(create_user)


schema = strawberry.Schema(query=Query, mutation=Mutation)

router = GraphQLRouter(schema, context_getter=get_context)
