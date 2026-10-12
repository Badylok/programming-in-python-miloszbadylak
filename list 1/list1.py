def divisible(numbers, divisor):
    """
    Returns a list of numbers from the input that are divisible by the given divisor.

    Args:
        numbers (list of int): The list of integers that we check for divisibility.
        divisor (int): The number by which we divide (cannot be 0).

    Returns:
        list of int: New list containing only divisible numbers.

    Pre-conditions:
        -numbers is a list of integers.
        -divisor is a non-zero integer.

    Post-conditions:
        -Returns a new list with elements from numbers divisible by divisor.

    Raises:
        TypeError: If 'numbers' is not a list, any of its elements is not an integer, or 'divisor' is not an integer.
        ValueError: If 'divisor' is equal to zero.
    """

    if not isinstance(numbers, list):
        raise TypeError("Numbers must be a list.")

    for number in numbers:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("All elements in numbers must be integers.")

    if not isinstance(divisor, int) or isinstance(divisor, bool):
        raise TypeError("Divisor must be an integer.")

    if divisor == 0:
        raise ValueError("Divisor cannot be zero!")

    result = []
    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    return result


def common(x, y):
    """
    Returns the intersection of two multisets represented as lists x and y.

    Args:
        x (list): First multiset.
        y (list): Second multiset.

    Returns:
        list: A list containing the common elements of x and y, including multiplicity.

    Pre-conditions:
        - x and y are lists.

    Post-conditions:
        - Returns a new list with the multiset intersection of x and y without modifying the original lists.

    Raises:
        TypeError: If x or y is not a list.
    """

    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("Both x and y must be lists.")

    intersections = []
    y_copy = list(y)
    for elements in x:
        if elements in y_copy:
            intersections.append(elements)
            y_copy.remove(elements)
    return intersections
