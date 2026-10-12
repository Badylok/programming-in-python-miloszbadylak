import list1


def test_divisible():
    assert list1.divisible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 4, 6, 8, 10]
    assert list1.divisible([], 3) == []
    assert list1.divisible([-20, -1, 0, 5], 5) == [-20, 0, 5]
    try:
        list1.divisible([1, 5, 10], 0)
        assert False
    except ValueError:
        pass
    try:
        list1.divisible(["xd", 2], 2)
        assert False
    except TypeError:
        pass
    print("All tests for divisible() passed!")


def test_common():
    assert list1.common([1, 2, 2, 3, 4, 5, 6], [2, 2, 4, 4, 7, 8]) == [2, 2, 4]
    assert list1.common([2, 2, 2, 2, 2, 2], [2, 2, 2, 3, 3]) == [2, 2, 2]
    assert list1.common([1, 2, 3, 4], [5, 6, 7, 8]) == []
    assert list1.common([], [1, 2, 3]) == []
    try:
        list1.common([1, 2, 3], 123)
        assert False
    except TypeError:
        pass
    print("All test for common() passed!")


test_divisible()
test_common()
