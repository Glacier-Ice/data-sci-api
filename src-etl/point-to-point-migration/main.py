import psycopg2
import json
from integration import get_p2p_overall_dataframe, get_index_overall_dataframe
from dateutils import all_dates_since_last_month, today
from sqlalchemy import create_engine

import os

config_path = os.getenv("CONFIG_PATH")
config = json.loads(config_path)


def insert_history():
    engine = create_engine(
        f"postgresql://{config['db_username']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    )
    df = get_p2p_overall_dataframe(all_dates_since_last_month(today()))
    df.to_sql("p2p_migration", engine, if_exists="replace", index=False, method="multi")


def insert_latest():
    engine = create_engine(
        f"postgresql://{config['db_username']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    )
    df = get_p2p_overall_dataframe()
    df.to_sql("p2p_migration", engine, if_exists="append", index=False, method="multi")


def insert_overwrite_index():
    engine = create_engine(
        f"postgresql://{config['db_username']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    )
    df = get_index_overall_dataframe()
    df.to_sql("migration_index", engine, if_exists="replace", index=False, method="multi")


if __name__ == "__main__":
    # insert_history()
    insert_latest()
    insert_overwrite_index()
