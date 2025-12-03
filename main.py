import sys

from stats import get_book_text, get_char_count, get_num_words, get_sorted_char_list


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        text = get_book_text(path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    char_list = get_sorted_char_list(get_char_count(text))

    for item in char_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
