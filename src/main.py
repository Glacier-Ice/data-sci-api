import argparse
import connexion
from swagger_ui_bundle import swagger_ui_3_path
import os
from connexion.resolver import RestyResolver
import prance
from pathlib import Path
from typing import Dict, Any
from src import config
import logging
import json


parser = argparse.ArgumentParser()
parser.add_argument("--host", default="0.0.0.0")
parser.add_argument("--port", type=int, default=8081)
args, _ = parser.parse_known_args()


def aggregate_specs(main_file: Path) -> Dict[str, Any]:
    """This function glues all seperate API Spec YML files together.
    This enales we keep a set of small YML files while being able
    to use something like $ref: 'another.yaml#/components/schemas/Foo'
    in the YML files.
    """
    parser = prance.ResolvingParser(str(main_file.absolute()), lazy=True, strict=True)
    parser.parse()
    return parser.specification


## STEP-1: Pass in Swagger Options
# Use OpenAPI Swagger page, and redirct SwaggerUI to root
options = {"swagger_path": swagger_ui_3_path, "swagger_url": ""}

## STEP-2: Initialize Flask/Connexion App
# Note this app is a wrapper around FlaskAPP, use app.app to access
# the actual Flask app
app = connexion.App(__name__, options=options)

## STEP-3: Configure the logger
logger = logging.getLogger(f"api.{__name__}")

## STEP-4: Load the config file from CONFIG_PATH and feeb it back to the Flask/Connexion
config_path = os.getenv("CONFIG_PATH")

# Note: this is a hack since Heroku doesn't support JSON config
if config_path and not Path(config_path).is_file():
    try:
        logger.info(f"Reading config file from string defined by $CONFIG_PATH.")
        api_config = config.Config.from_string(string=config_path, flask_config_values=app.app.config)
    except (json.decoder.JSONDecodeError, TypeError):
        logger.warning("Invalid config or config_path provided!")
else:
    # Use the backup default config
    if not config_path:
        logger.warning("Attempting to use the default config.")
        config_path = Path(__file__).parent / "tests/data/example_config.json"
    logger.info(f"Using config file at {config_path}")
    api_config = config.Config.from_file(config_path=config_path, flask_config_values=app.app.config)

app.app.config = api_config

## STEP-5: Feed in the Swagger Spec
app.add_api(
    aggregate_specs(Path(__file__).parent / "swagger/api.yml"), validate_responses=True, resolver=RestyResolver("src.api"),
)


if __name__ == "__main__":
    app.run(host=args.host, port=os.environ.get("FC_SERVER_PORT", args.port), debug=False)
