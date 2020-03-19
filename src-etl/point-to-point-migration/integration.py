import json
import logging
import os

import pandas as pd
from crawl import crawl_history, crawl_p2p
from dateutils import yesterday
from filemap import FilepathMapper
from read_assets import get_city_code_table
from variables import LOGGER_LEVEL

logger = logging.getLogger()
logger.setLevel(LOGGER_LEVEL)


def update_history_if_outdated(direction, city_id):
    path = FilepathMapper.history("110000", direction)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            res = f.read()
        if yesterday() not in res:
            logger.info("Obtaining the latest history data.")
            crawl_history(direction)
    else:
        logger.info("Obtaining the history data for the first time.")
        crawl_history(direction)


def load_history(date, city_id):
    update_history_if_outdated("in", city_id)
    path = FilepathMapper.history(city_id, "in")
    if os.path.exists(path):
        logger.info(f"Reading <{city_id}> <{date}> history data")
        with open(path, "r", encoding="utf-8") as f:
            res = f.read()
        return json.loads(res.split("(")[-1][:-1])["data"]["list"]
    else:
        return None


def load_p2p(date, city_id):
    path = FilepathMapper.p2p(date, city_id, "in")
    if not os.path.exists(path):
        logger.info("Obtaining the latest point to point data")
        crawl_p2p("in", date)

    logger.info(f"Reading <{city_id}> <{date}> point to point data")
    with open(path, "r", encoding="utf-8") as f:
        res = f.read()

    return json.loads(res.split("(")[-1][:-1])["data"]["list"]


def get_p2p_overall_dataframe(dates=[yesterday()]):
    res = []
    for date in dates:
        for _, row in get_city_code_table().iterrows():
            history_curve = load_history(date, row.adcode)
            if history_curve is None:
                continue
            move_data = load_p2p(date, row.adcode)
            for record in move_data:
                from_city = row["name"]
                if from_city[-1] == "市":
                    from_city = from_city[:-1]

                to_city = record["city_name"]
                if to_city[-1] == "市":
                    to_city = to_city[:-1]

                to_province = record["province_name"]
                if to_province[-1] in ["省", "市"]:
                    to_province = to_province[:-1]

                new_entry = {
                    "m_date": pd.to_datetime(date),
                    "from_city": from_city,
                    "to_city": to_city,
                    "to_province": to_province,
                    "percentage": record["value"],
                    "migration_index": history_curve[date],
                }
                res.append(new_entry)
    return pd.DataFrame(res)


def get_index_overall_dataframe(date=yesterday()):
    res = []
    for _, row in get_city_code_table().iterrows():
        history_curve = load_history(date, row.adcode)
        if history_curve is None:
            continue
        city = row["name"]
        if city[-1] in ["省", "市"]:
            city = city[:-1]
        for this_date in history_curve.keys():
            new_entry = {"m_date": pd.to_datetime(this_date), "city": city, "migration_index": history_curve[date]}
            res.append(new_entry)

    return pd.DataFrame(res)


if __name__ == "__main__":
    res = get_p2p_overall_dataframe()
    res.info()
    print(res.head(10))
