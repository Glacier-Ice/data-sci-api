import psycopg2
from flask import current_app


config = current_app.config
DB_SETTINGS = {
    "database": config["db_name"],
    "user": config["db_username"],
    "password": config["db_password"],
    "host": config["db_host"],
    "port": config["db_port"],
}


def query(sql: str, db_settings=DB_SETTINGS) -> list:
    """Connect to the database based on DB_SETTINGS and execute SQL."""
    with psycopg2.connect(**db_settings) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def get_tables() -> list:
    """Get the tables in the current database."""
    SQL = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"""
    return query(sql=SQL)
