import os

import uvicorn

from hello_graphql.main import create_app

os.environ.setdefault("APP_SETTINGS_MODULE", "hello_graphql.settings")

app = create_app()


def runserver():
    uvicorn.run(app, port=8899)
