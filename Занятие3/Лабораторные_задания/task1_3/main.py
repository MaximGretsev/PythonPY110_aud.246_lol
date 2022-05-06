OUTPUT_FILE = "output.txt"


def task(n):
    with open(OUTPUT_FILE, "w") as f:
        f.write(",".join(str(i ** 2) for i in range(1, n + 1)))
        f.write("\n")


if __name__ == "__main__":
    task(20)

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
