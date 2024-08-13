from . import create_app

# from dotenv import dotenv_values
# config = dotenv_values(".env")

from dotenv import load_dotenv
load_dotenv() 

from .procesess import my_feature_thread
from threading import Thread

t1 = Thread(target=my_feature_thread, args=())
t1.start()
# t1.join()

app = create_app()
