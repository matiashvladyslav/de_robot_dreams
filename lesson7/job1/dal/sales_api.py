import requests
import os
from typing import List, Dict, Any

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    print("*"*80)
    print("get_sales")
    page_num = 1
    data = []
    while True:
        response = requests.get(f"{API_URL}/sales?date={date}&page={page_num}", headers={'Authorization': AUTH_TOKEN})
        if response.ok:
            data.extend(response.json())
            page_num += 1
        else:
            break

    return data
