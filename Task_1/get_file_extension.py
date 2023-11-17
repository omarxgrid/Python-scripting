import sys


def get_file_extension(filename):
    ext = filename.split('.')
    if len(ext) < 2:
        raise Exception("Please enter a file name with its extension")
    else:
        print(ext[1])


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    get_file_extension(filename)


if __name__ == "__main___":
    main()
