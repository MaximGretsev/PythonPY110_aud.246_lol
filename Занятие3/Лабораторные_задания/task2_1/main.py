import json


def task(n) -> str:
    dict_numbers = {i: i ** 2 for i in range(1, n + 1)}  # TODO c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)  # TODO сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task(10))
