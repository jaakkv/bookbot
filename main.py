import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = number_of_words(text)
    chars_dict = number_of_characters(text)
    print_report(book_path, num_of_words, chars_dict)

if __name__ == '__main__':
    main()