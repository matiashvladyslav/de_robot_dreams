from lesson_02.ht_template.job2.dal import local_disk


def save_sales_from_json_to_avro(raw_dir: str, stg_dir: str) -> None:
    # 1. get data from the API
    data = local_disk.read_json_from_disk(raw_dir)

    print("\tI'm in get_sales(...) function!")

    # 2. save data to disk
    local_disk.save_to_avro(data, stg_dir)

    return None
