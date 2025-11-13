from dotenv import load_dotenv
import os

load_dotenv()

MINDSDB_URL = os.getenv("MINDSDB_URL")
MINDSDB_USER = os.getenv("MINDSDB_USER")
MINDSDB_PASSWORD = os.getenv("MINDSDB_PASSWORD")

from mindsdb_sdk import connect

def get_server():
    return connect(MINDSDB_URL, login=MINDSDB_USER, password=MINDSDB_PASSWORD)

