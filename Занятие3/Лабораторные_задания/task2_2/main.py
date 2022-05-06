import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename) as f:
        obj = json.load(f)

    with open(output_filename, 'w') as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")


# def from_json_file():
#     with open(INPUT_FILE) as f:
#         python_object = json.load(f)
#         return python_object
#
#
# def to_json_file(python_object):
#     json.dump(python_object, f, indent=4, ensure_ascii=False)
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#         pass