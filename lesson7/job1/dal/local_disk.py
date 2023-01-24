import os
import shutil
import json
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    with open(f"{path}/sales_{os.path.basename(path)}.json", 'w') as f:
        json.dump(json_content, f, ensure_ascii=False, indent=4)

    return None
