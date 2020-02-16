from src.config import Config
from pathlib import Path


def test_config_can_be_loaded():
    config = Config(config_path=f"{Path(__file__).parent}/data/example_config.json")
    assert config.db_host == "test_db_host"
