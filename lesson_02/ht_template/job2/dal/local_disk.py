import os
import shutil
import json
from fastavro import writer, parse_schema
from typing import List, Dict, Any


def save_to_avro(json_content: List[Dict[str, Any]], path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    schema = {
        'doc': 'Sales',
        'name': 'Sales',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'},
        ],
    }
    parsed_schema = parse_schema(schema)

    with open(f'{path}/sales_{os.path.basename(path)}.avro', 'wb') as out:
        writer(out, parsed_schema, json_content)

    return None


def read_json_from_disk(path: str) -> List[Dict[str, Any]]:
    with open(f"{path}/sales_{os.path.basename(path)}.json") as f:
        data = json.load(f)

    return data
