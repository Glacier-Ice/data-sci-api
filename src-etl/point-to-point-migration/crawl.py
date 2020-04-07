import logging
import time

import requests

from filemap import FilepathMapper
from read_assets import get_city_codes
from dateutils import yesterday
from variables import LOGGER_LEVEL

logger = logging.getLogger()
logger.setLevel(LOGGER_LEVEL)

SLEEP_SEC = 1

def crawl_p2p(direction: str, date=yesterday()):
    assert direction in ["in", "out"]
    city_code = get_city_codes()
    total = len(city_code)
    for i, city_record in enumerate(get_city_codes()):
        time.sleep(SLEEP_SEC)
        city_id = city_record["code"]
        logger.info(f"[{i+1}/{total}]: {city_record['city']} ({city_id})")

        query = f"https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={city_id}&type=move_{direction}&date={date}"
        logger.info(f"Getting {query}")
        res = requests.get(query)
        if res.status_code == 200:
            logger.info("Success.")
            with open(FilepathMapper.p2p(date, city_id, direction), "w", encoding="utf-8") as f:
                f.write(res.text)
        else:
            logger.warning(f"Bad response code {res.status_code} for {city_record['city']}")


def crawl_history(direction: str, date=yesterday()):
    assert direction in ["in", "out"]
    city_code = get_city_codes()
    total = len(city_code)
    for i, city_record in enumerate(city_code):
        time.sleep(SLEEP_SEC)
        city_id = city_record["code"]
        logger.info(f"[{i+1}/{total}]: {city_record['city']} ({city_id})")

        query = (
            "https://huiyan.baidu.com/migration/historycurve.jsonp"
            + f"?dt=city&id={city_id}&type=move_{direction}&startDate=20200101&endDate={date}"
        )
        logger.info(f"Getting {query}")
        res = requests.get(query)
        if res.status_code == 200:
            logger.info("Success.")
            with open(FilepathMapper.history(city_id, direction), "w", encoding="utf-8") as f:
                f.write(res.text)
        else:
            logger.warning(f"Bad response code {res.status_code} for {city_record['city']}")
