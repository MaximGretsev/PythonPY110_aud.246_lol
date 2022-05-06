from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # TODO заменить на map и filter

    for num in numbers:  # TODO напечатать первые 10 чисел
        print(num)  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
