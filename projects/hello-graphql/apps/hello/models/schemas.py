import strawberry
from strawberry import types


@strawberry.type
class User:
    username: str
    name: str


def get_user(username: str, info: types.Info):
    return User(username=username, name="John Doe")


@strawberry.input
class UserInput:
    username: str
    name: str


def create_user(username: str, name: str, info: types.Info) -> User:
    return User(username=username, name=name)
