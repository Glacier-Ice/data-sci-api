from src.config import Config
from pathlib import Path
import json


def test_config_can_be_loaded_from_file():
    file = f"{Path(__file__).parent}/data/example_config.json"
    config = Config.from_file(file)
    assert config.db_host == "test_db_host"


def test_config_can_be_loaded_from_string():
    with open(f"{Path(__file__).parent}/data/example_config.json") as fp:
        string = json.dumps(json.load(fp))
    config = Config.from_string(string)
    assert config.db_host == "test_db_host"
