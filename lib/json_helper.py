import json


def read_json(jsonpath: str) -> dict:
    with open(jsonpath, "r") as f:
        json_data = json.load(f)
    return json_data


def write_json(jsonpath: str, data: dict):
    with open(jsonpath, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
