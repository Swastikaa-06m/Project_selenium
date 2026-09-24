import json
from pathlib import Path


def load_test_data():
    """Load test data from the JSON file."""

    data_file = (
        Path(__file__).resolve().parent.parent
        / "test_data"
        / "test_data.json"
    )

    with open(data_file, "r", encoding="utf-8") as file:
        return json.load(file)