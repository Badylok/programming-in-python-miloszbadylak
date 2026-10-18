def dna_complement(orig_strand):
    """
    Returns complementary DNA strand usint the Watson-Crick pairing rules.

    Args:
        orig_strand (str): Inputed DNA strand

    Returns:
        str: Reversed DNA base pairs.

    Pre-conditions:
        - 'orig_strand' must be a string.
        - 'orig_strand' must contain only bases "A", "T", "C" and "G".

    Post-conditions:
        - Returned string has the exact same length as the input string.
    Raises:
        TypeError: 'orig_strand' is not a string
        ValueError: 'orig_strand' has invalid DNA base
    """

    if not isinstance(orig_strand, str):
        raise TypeError("'orig_strand' must be a string.")

    orig_strand = orig_strand.upper()

    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}

    for base in orig_strand:
        if base not in pairs:
            raise ValueError("Invalid DNA base.")

    complement = ""

    for base in orig_strand:
        complement = complement + pairs[base]

    return complement[::-1]


# test

def test_dna_complement():
    assert dna_complement("ATCG") == "CGAT"
    assert dna_complement("atcg") == "CGAT"
    
    try:
        dna_complement("ABCD")
        assert False
    except ValueError:
        pass
    
    try:
        dna_complement(123)
        assert False
    except TypeError:
        pass
    
    print("All tests for dna_complement() passed!")

if __name__ == "__main__":
    test_dna_complement()

