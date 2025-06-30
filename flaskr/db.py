import psycopg2
from flask import g


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
          database="dataengpipeline",
          user="postgres",
          password="postgres",
          host="localhost", port="5432"
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()