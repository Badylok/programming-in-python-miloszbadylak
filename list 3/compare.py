import argparse
from shingle import shingles

if __name__ == "__main__":
    """Compares two text files by calculating the Jaccard similarity between their k-shingles."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True)
    parser.add_argument("--target", type=str, required=True)
    parser.add_argument("-k", type=int, required=True)
    parser.add_argument("--remove_punctuation", action="store_true")
    args = parser.parse_args()

    with open(args.query, "r", encoding="utf-8") as f:
        text1 = f.read()

    with open(args.target, "r", encoding="utf-8") as f:
        text2 = f.read()

    if args.remove_punctuation:
        sings = ".,?!:;\"'()[]{}<>"
        for s in sings:
            text1 = text1.replace(s, "")
            text2 = text2.replace(s, "")

    shingle1 = shingles(text1.split(), args.k)
    shingle2 = shingles(text2.split(), args.k)

    czesc_wspolna = sum((shingle1 & shingle2).values())
    suma_wszystkich = sum((shingle1 | shingle2).values())

    if suma_wszystkich == 0:
        similarity = 1.0
    else:
        similarity = czesc_wspolna / suma_wszystkich

    print(f"Jaccard similarity: {similarity:.4f}")
