import random
import matplotlib.pyplot as plt


def random_walk(n):
    """
      Simulates two-dimensional random walk until the distance reach 'n'.

    Args:
        n (int): Maximum allowed distance from starting point.

    Returns:
        list of tuples: List of coordinates (x, y) which represents path of the walk.

    Pre-conditions:
        - n must be positive integer

    Post-conditions:
        - Returns a list which starts with (0,0) and ends when the distance reach 'n'.

    Raises:
        TypeError: n is not an integer
        ValueError: n is non-positive
    """

    if not isinstance(n, int):
        raise TypeError("'n' must be an integer.")

    if n <= 0:
        raise ValueError("'n' must be positive.")

    x = 0
    y = 0
    coordinates = [(0, 0)]

    while (x**2 + y**2) ** 0.5 <= n:

        direction = random.choice(["up", "down", "right", "left"])

        if direction == "up":
            y = y + 1
        elif direction == "down":
            y = y - 1
        elif direction == "right":
            x = x + 1
        elif direction == "left":
            x = x - 1

        coordinates.append((x, y))

    return coordinates


# test


def test_random_walk():
    assert random_walk(10)[0] == (0, 0)

    try:
        random_walk(0)
        assert False
    except ValueError:
        pass

    try:
        random_walk("ten")
        assert False
    except TypeError:
        pass


# output

if __name__ == "__main__":
    test_random_walk()
    n = 100
    coordinates = random_walk(n)
    x, y = zip(*coordinates)

    plt.plot(x, y, marker="o", linestyle="-", markersize=2)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Walker's Trajectory")
    plt.grid(True)
    plt.show()
