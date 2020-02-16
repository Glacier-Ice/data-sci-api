import os
from variables import BASE_DIR

TEMP_DIR = "temp"


class FilepathMapper:
    @staticmethod
    def p2p(date, city_id, direction):
        return os.path.join(BASE_DIR, TEMP_DIR, f"move_{direction}_p2p_{date}_{city_id}.txt")

    @staticmethod
    def history(city_id, direction):
        return os.path.join(BASE_DIR, TEMP_DIR, f"move_{direction}_history_{city_id}.txt")
