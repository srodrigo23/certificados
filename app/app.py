from . import create_app

from dotenv import dotenv_values
config = dotenv_values(".env")

app = create_app(env_values=config)
