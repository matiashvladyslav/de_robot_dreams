from lesson_02.ht_template.job1.dal import local_disk, sales_api


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    # 1. get data from the API
    data = sales_api.get_sales(date)

    print("\tI'm in get_sales(...) function!")

    # 2. save data to disk
    local_disk.save_to_disk(data, raw_dir)

    return None
