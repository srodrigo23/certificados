from . import create_app

# from dotenv import dotenv_values
# config = dotenv_values(".env")

from dotenv import load_dotenv
load_dotenv() 

app = create_app()
