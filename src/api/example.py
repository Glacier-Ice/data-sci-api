"""This is just an example file showing how to create api handlers."""
from connexion.exceptions import ProblemException

EXAMPLE_DATA = [
    {"time": "2019-01-01T00:12:33.001Z", "name": "Naruto"},
    {"time": "2020-01-01T00:12:33.001Z", "name": "Conan"},
]


def get_examples() -> list:
    """Get all examples."""
    return EXAMPLE_DATA


def get_example_by_name(name: str) -> dict:
    """Query example by name."""
    for example in EXAMPLE_DATA:
        if example["name"] == name:
            return example
    raise ProblemException(status=404, detail=f"Cannot find example {name}!")
