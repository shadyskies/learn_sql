from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def connect(database):
    load_dotenv()
    db_connection_url = f"mysql+mysqldb://django_projects:{os.getenv('db_pwd')}@localhost/{database}"
    engine = create_engine(db_connection_url)
    return engine


def query_db(engine, query):
    cur = engine.raw_connection().cursor()
    cur.execute(query)
    return list(cur.fetchall())
