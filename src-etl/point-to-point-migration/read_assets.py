import pandas as pd
from typing import Dict
import os
from variables import BASE_DIR


def get_city_code_table() -> pd.DataFrame:
    with open(os.path.join(BASE_DIR, "assets", "city_codes.csv"), "r", encoding="utf-8") as f:
        table = pd.read_csv(f)

    table.loc[table.name == "恩施土家族苗族自治州", "name"] = "恩施州"
    return table


def __get_traffic_table() -> pd.DataFrame:
    with open(os.path.join(BASE_DIR, "assets", "confirm_vs_traffic.csv"), "r", encoding="utf-8",) as f:
        table = pd.read_csv(f)

    return table


def get_city_codes() -> Dict:
    city_code_table = get_city_code_table()
    city_codes = []
    for city in __get_traffic_table().city:
        find_1 = city_code_table[city_code_table.name == city]
        find_2 = city_code_table[city_code_table.name == city + "市"]
        if len(find_1) == 1:
            city_codes.append({"city": city, "code": find_1.adcode.values[0]})
        elif len(find_2) == 1:
            city_codes.append({"city": city, "code": find_2.adcode.values[0]})
    city_codes.append({"city": "武汉", "code": 420100})
    return city_codes
