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


# test:

def test_common():
    assert common([1, 2, 2, 3, 4, 5, 6], [2, 2, 4, 4, 7, 8]) == [2, 2, 4]
    assert common([2, 2, 2, 2, 2, 2], [2, 2, 2, 3, 3]) == [2, 2, 2]
    assert common([1, 2, 3, 4], [5, 6, 7, 8]) == []
    assert common([], [1, 2, 3]) == []
    try:
        common([1, 2, 3], 123)
        assert False
    except TypeError:
        pass
    print("All tests for common() passed!")
    
    test_common()