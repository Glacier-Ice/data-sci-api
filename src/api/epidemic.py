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


def get_all(granularity: str, limit: int = 0):
    """Fetch all of the available epidemic data based on GRANULARITY and LIMIT."""
    if granularity == "province":
        TABLE = "area_province"
        deserilize_func = deserilize_edpidemic_province
    else:
        TABLE = "area_city"
        deserilize_func = deserilize_edpidemic_city

    SQL = f"SELECT * FROM {TABLE}"
    if limit > 0:
        SQL += f" LIMIT {limit}"

    results = database.query(sql=SQL)
    return list(map(deserilize_func, results))


def query():
    pass
