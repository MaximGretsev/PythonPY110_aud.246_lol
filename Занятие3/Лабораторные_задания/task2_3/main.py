import json


def task():
    out_name = "output.json"
    filename = "input.json"
    with open(filename) as f:
        obj = json.load(f)
    #     for i in obj:
    #         r = [i['score'] for i in obj]
    # return max(r)
    result = max(obj, key=lambda item: item['score'])
    out_name = "output.json"
    with open(out_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    return result


if __name__ == "__main__":
    print(task())
