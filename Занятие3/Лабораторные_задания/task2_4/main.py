import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_parse = json.load(f)

    gen_exr = (i["contains_improvement_appeals"] for i in json_parse)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
