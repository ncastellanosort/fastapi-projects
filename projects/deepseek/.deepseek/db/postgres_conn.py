from dotenv import load_dotenv
import os
from sqlmodel import create_engine, Session

load_dotenv()

URL = os.getenv('URL_DATABASE')

engine = create_engine(URL)

def get_db_session():
    with Session(engine) as session:
        yield session