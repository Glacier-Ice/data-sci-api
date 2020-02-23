from src.core import database
import datetime

DATE_FORMAT: str = "%Y-%m-%d"
TABLE = "p2p_migration"


def deserialize_migration_data(record: tuple) -> dict:
    return {
        "m_date": record[0].strftime(DATE_FORMAT),
        "from_city": str(record[1]),
        "to_city": str(record[2]),
        "to_province": str(record[3]),
        "percentage": float(record[4]),
        "migration_index": float(record[5]),
    }


def get_all(limit: int = 0) -> list:
    if limit <= 0:
        limit - None
    query = """select * from {table} limit %(limit)s""".format(table=TABLE)
    results = database.query(sql=query, table=TABLE, limit=limit)
    return list(map(deserialize_migration_data, results))


def query(start: str = None, end: str = None, limit: int = 0) -> list:
    if start:
        start = datetime.datetime.strptime(start, DATE_FORMAT)
    if end:
        end = datetime.datetime.strptime(end, DATE_FORMAT)

    if limit <= 0:
        limit = None

    query = """
    select * from {table} as t
    where
    (%(start)s is null or %(start)s <= t.m_date)
    AND
    (%(end)s is null or %(end)s >= t.m_date)
    limit %(limit)s
    """.format(
        table=TABLE
    )

    results = database.query(sql=query, limit=limit, start=start, end=end)
    return list(map(deserialize_migration_data, results))
