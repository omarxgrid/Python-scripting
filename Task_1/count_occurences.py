import sys

def count_occurence(words):
    counts = {}
    for char in words:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        print(f"{char}: {count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <words>")
        sys.exit(1)
    words = sys.argv[1]
    count_occurence(words)


if __name__ == "__main__":
    main()
