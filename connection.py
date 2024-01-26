
from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os
load_dotenv()
key=os.getenv("db_key")



conn_str = f'{key}'
engine = create_engine(conn_str)