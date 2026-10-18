def subsets(x):
    """
    Returns all possible subsets of x.
    
    Args:
        x: Main list, which we create subsets of.
    
    Returns:
        list: A list containing all possible subsets of x.
    
    Pre-conditions:
        - x must be a set or a list.
        
    Post-conditions:
        - Returns a new list with all subsets of x.
        
    Raises:
        TypeError: If x is not a set or a list.
    """
    
    if not isinstance(x, (set, list)):
        raise TypeError("x must be a set or a list.")
        
    result = [[]]
    for element in x:
        new_subsets = []
        for subset in result:
            new = subset + [element]
            new_subsets.append(new)
        result.extend(new_subsets)
    return result

# test:

def test_subsets():
    assert subsets(["a", "b", "c"]) == [
        [],
        ["a"],
        ["b"],
        ["a", "b"],
        ["c"],
        ["a", "c"],
        ["b", "c"],
        ["a", "b", "c"],
    ]
    assert subsets([1, 2]) == [[], [1], [2], [1, 2]]
    assert subsets([]) == [[]]
    assert subsets([47]) == [[], [47]]
    try:
        subsets(123)
        assert False
    except TypeError:
        pass
    print("All tests for subsets() passed!")
    
    test_subsets()