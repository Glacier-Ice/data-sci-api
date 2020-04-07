import psycopg2
import json
from integration import get_p2p_overall_dataframe, get_index_overall_dataframe
from dateutils import all_dates_since_last_month, today, from_date_to_date, yesterday
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

config_path = os.getenv("CONFIG_PATH")
config = json.loads(config_path)


def insert_overwrite_history():
    engine = create_engine(
        f"postgresql://{config['db_username']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    )
    df = get_p2p_overall_dataframe(all_dates_since_last_month(today()))
    df.to_sql("p2p_migration", engine, if_exists="replace", index=False, method="multi")


def insert_latest():
    engine = create_engine(
        f"postgresql://{config['db_username']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    )
    session_fact = sessionmaker(bind=engine)
    session = session_fact()
    last_sql_date = session.execute(
            "SELECT MAX(m_date) from p2p_migration"
        ).fetchall()[0][0].strftime('%Y%m%d')
    print(last_sql_date)
    df = get_p2p_overall_dataframe(from_date_to_date(last_sql_date, yesterday()))
    print(df)
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
