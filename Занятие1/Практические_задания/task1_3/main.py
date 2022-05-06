def get_distance(point: tuple) -> int:
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def task(points: list) -> tuple:
    # TODO заменить на функцию max и функцию get_distance
    list_distances = list(map(get_distance, points))
    max_distance = max(list_distances)

    for index, current_distance in enumerate(list_distances):
        if current_distance == max_distance:
            return points[index]


if __name__ == "__main__":
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(task(pts))
