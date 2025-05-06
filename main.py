import sys
from stats import get_word_count, count_characters, sort_chars


def get_book_text(filepath: str):
    with open(filepath, "r") as bookFile:
        file_contents = bookFile.read()
    return file_contents


def generate_report(filepath: str, word_count: int, char_list: list[dict]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in char_list:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")


def main():
    # filepath = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = f"{sys.argv[1]}"
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    char_count = count_characters(text)
    sorted_char_count = sort_chars(char_count)
    generate_report(filepath, word_count, sorted_char_count)


if __name__ == "__main__":
    main()
