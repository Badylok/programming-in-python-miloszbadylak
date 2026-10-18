import ex5


def find_genes(dna_sequence):
    """
    Searchs for all potential genes in given DNA strand.

    A gene starts with 'ATG' and ends with 'TAG', 'TAA', or 'TGA',
    has a length that is a multiple of 3 and contains no internal stop codons.

    Args:
        dna_sequence(str): Inputed DNA sequence to search.

    Returns:
        list of str: A list of all found gene sequences.

    Pre-conditions:
        - 'dna_sequence' must be a string.
        - 'dna_sequence' must contain only bases "A", "T", "C" and "G".

    Post-conditions:
        - Returned list contains only strings whose length is a multiple of 3.

    Raises:
        TypeError: 'dna_sequence' is not a string.
        ValueError: 'dna_sequence' has an invalid DNA base.
    """

    if not isinstance(dna_sequence, str):
        raise TypeError("'dna_sequence' must be a string.")

    dna_sequence = dna_sequence.upper()
    valid_bases = {"A", "T", "C", "G"}

    for base in dna_sequence:
        if base not in valid_bases:
            raise ValueError("Invalid DNA base.")

    genes = []
    n = len(dna_sequence)

    for i in range(n - 2):

        if dna_sequence[i : i + 3] == "ATG":

            for j in range(i + 3, n - 2, 3):
                codon = dna_sequence[j : j + 3]

                if codon in ["TAA", "TAG", "TGA"]:
                    gene = dna_sequence[i : j + 3]
                    genes.append(gene)
                    break
    return genes


# test


def test_find_genes():
    assert find_genes("CGATGCCCTAG") == ["ATGCCCTAG"]
    assert find_genes("CTAGGGATCG") == []

    try:
        find_genes("ABCD")
        assert False
    except ValueError:
        pass

    try:
        find_genes(123)
        assert False
    except TypeError:
        pass

    print("All tests for find_genes() passed!")




if __name__ == "__main__":
    test_find_genes()

    try:
        dna = input("\nEnter a DNA sequence: ").upper()

        print("\nOriginal genes:")
        print(find_genes(dna))

        comp_dna = ex5.dna_complement(dna)

        print("\nGenes in complementary:")
        print(find_genes(comp_dna))

    except ValueError:
        print("\nValue Error: Please enter only A, C, G, T bases.")
    except TypeError:
        print("\nType Error: The input must be a text string.")
