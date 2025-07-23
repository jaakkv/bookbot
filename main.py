from stats import *

def main():
    result = []

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(number_of_words('books/frankenstein.txt'))
    print("--------- Character Count -------")
    result = number_of_characters('books/frankenstein.txt')
    result.sort(reverse=True, key=sort_dictionary)
    for item in result:
        print(f"{item["char"]}: {item['num']}")
    print("============= END ===============")
if __name__ == '__main__':
    main()