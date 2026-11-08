from collections import Counter
import argparse


def shingles(t, k):
    """
    Extracts k-shingles (k-grams) from a list of tokens and counts their frequencies.

    Args:
        t (list): A list of tokens (words) extracted from a text.
        k (int): The size of the shingle (number of consecutive tokens).

    Returns:
        Counter: A multiset (collections.Counter object) containing k-shingles as keys and their frequencies as values.

    Raises:
        TypeError: If 't' is not a list or 'k' is not an int.
        ValueError: If 'k' is less than or equal to 0.
    """

    if not isinstance(k, int):
        raise TypeError("'k' must be an int.")
    if k <= 0:
        raise ValueError("'k' must be positive")
    if not isinstance(t, list):
        raise TypeError("'t' must be a list.")

    k_mers = []

    for i in range(0, len(t) - k + 1):
        k_gram = tuple(t[i : i + k])
        k_mers.append(k_gram)

    return Counter(k_mers)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-k", type=int)
    parser.add_argument("-n", type=int)
    args = parser.parse_args()

    all_tokens = []

    while True:
        try:
            text = input()
            all_tokens.extend(text.split())
        except EOFError:
            break

    print(shingles(all_tokens, args.k).most_common(args.n))
