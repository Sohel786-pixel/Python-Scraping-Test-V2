
import json

from src import parse_categories


def test_parse_categories():
    categories = parse_categories()
    with open(r"C:\Users\sohel\Downloads\categories.json.gz") as f:
        expected_categories = json.load(f)
    assert categories == expected_categories
