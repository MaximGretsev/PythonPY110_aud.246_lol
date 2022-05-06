import json


def task():
    filename = "input.json"
    out_file = 'output.json'
    with open(filename) as f:
        json_data = json.load(f)
    res = sorted(json_data, key=lambda item: item['length'])
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
    return res


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

