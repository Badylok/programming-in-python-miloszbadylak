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

# test:

def test_divisible():
    assert divisible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 4, 6, 8, 10]
    assert divisible([], 3) == []
    assert divisible([-20, -1, 0, 5], 5) == [-20, 0, 5]
    try:
        divisible([1, 5, 10], 0)
        assert False
    except ValueError:
        pass
    try:
        divisible(["xd", 2], 2)
        assert False
    except TypeError:
        pass
    print("All tests for divisible() passed!")
    
    test_divisible()