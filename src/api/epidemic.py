from src.core import database
import datetime


DATE_FORMAT: str = "%Y-%m-%d"


def deserilize_edpidemic_city(record: tuple) -> dict:
    """Deserilize the DB records to API formats for by city data."""
    return {
        "id": int(record[0]),
        "curday": record[1].strftime(DATE_FORMAT),
        "city_name": str(record[2]),
        "city_code": str(record[3]),
        "confirmed_count": int(record[4]),
        "cured_count": int(record[5]),
        "dead_count": int(record[6]),
        "suspected_count": int(record[7]),
    }


def deserilize_edpidemic_province(record: tuple) -> dict:
    """Deserilize the DB records to API formats for by province data."""
    return {
        "id": int(record[0]),
        "curday": record[1].strftime(DATE_FORMAT),
        "province_name": str(record[2]),
        "province_code": str(record[3]),
        "confirmed_count": int(record[4]),
        "cured_count": int(record[5]),
        "dead_count": int(record[6]),
        "suspected_count": int(record[7]),
    }


def get_all(granularity: str, limit: int = 0) -> list:
    """Fetch all of the available epidemic data based on GRANULARITY and LIMIT."""
    if granularity == "province":
        table = "area_province"
        deserilize_func = deserilize_edpidemic_province
    else:
        table = "area_city"
        deserilize_func = deserilize_edpidemic_city

    if limit <= 0:
        limit = None

    # table name is not transormbale by psycopg2
    SQL = """SELECT * FROM {table} LIMIT %(limit)s""".format(table=table)

    results = database.query(sql=SQL, table=table, limit=limit)
    return list(map(deserilize_func, results))


def query(name: list, granularity: str, start: str = None, end: str = None, limit: int = 0) -> list:
    """Get epidemic data by specific criterias."""
    if granularity == "province":
        table = "area_province"
        deserilize_func = deserilize_edpidemic_province
    else:
        table = "area_city"
        deserilize_func = deserilize_edpidemic_city

    if start:
        start = datetime.datetime.strptime(start, DATE_FORMAT)

    if end:
        end = datetime.datetime.strptime(end, DATE_FORMAT)

    if limit <= 0:
        limit = None

    # table name is not transormbale by psycopg2
    SQL = """SELECT * FROM {table} AS t 
             WHERE 
             (%(start)s is null or %(start)s <= t.curday) 
             AND 
             (%(end)s is null or %(end)s >= t.curday) 
             LIMIT %(limit)s""".format(
        table=table
    )
    results = database.query(sql=SQL, limit=limit, start=start, end=end)
    return list(map(deserilize_func, results))
