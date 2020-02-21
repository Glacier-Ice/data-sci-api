from src.core import database


def deserilize_edpidemic_city(record: tuple) -> dict:
    """Deserilize the DB records to API formats for by city data."""
    return {
        "id": int(record[0]),
        "curday": record[1].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
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
        "curday": record[1].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
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

    SQL = """SELECT * FROM %(table) 
             LIMIT %(limit)"""

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
        pass
    if limit <= 0:
        limit = None

    SQL = """SELECT * 
             FROM %(table) 
             WHERE
                (%(start)s is null or %(start)s = age)
                AND
                (%(age)s is null or %(age)s = age)
             LIMIT %(limit)"""
    results = database.query(sql=SQL, table=table, limit=limit, start=start, end=end)
    return list(map(deserilize_func, results))
