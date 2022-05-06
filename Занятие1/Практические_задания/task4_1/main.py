from itertools import count


def task():
    iterator_numbers = count(1, 1)  # бесконечный счетчик натуральных чисел, который занимает конечный размер в памяти

    print(f"Является ли объект итератором? {iterator_numbers is iter(iterator_numbers)}")  # Итератор
    for _ in range(5):  # распечатать первые 5 натуральных чисел
        print(...)  # TODO как получить от итератора следующий объект?

    print("Выполнение некоторого кода ...")

    for _ in range(5):  # распечатать следующие 5 натуральных чисел
        print(...)  # TODO как получить от итератора следующий объект?


if __name__ == "__main__":
    task()
