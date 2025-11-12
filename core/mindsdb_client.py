from dotenv import load_dotenv
import os

load_dotenv()

MINDSDB_URL = os.getenv("MINDSDB_URL")
MINDSDB_USER = os.getenv("MINDSDB_USER")
MINDSDB_PASSWORD = os.getenv("MINDSDB_PASSWORD")

from mindsdb_sdk import connect

def get_server():
    return connect(MINDSDB_URL, login=MINDSDB_USER, password=MINDSDB_PASSWORD)
# from mindsdb_sdk import connect

# def get_server():
#     return connect(
#         "http://192.168.1.182:47434",
#         login="hasina.oely@gmail.com", 
#         password="9e57aa775ea77b02bac7413e7ad1d55fa5306c4cf478054a1e0bd6d35ddfbf5a"
#     )
