def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
        words = text.split()
        return len(words)

def number_of_characters(text):
    char_dict = {}

    for char in text:
        if char.isalpha():
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1

    result = [{"char": c, "num": n} for c, n in char_dict.items()]
    return result

def sort_dictionary(dict_item):
    return dict_item["num"]

def print_report(book_path, num_of_words, chars_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("----------- Character Count ----------")
    chars_dict.sort(reverse=True, key=sort_dictionary)
    for dict_item in chars_dict:
        print(f"{dict_item["char"]}: {dict_item['num']}")
    print("============= END ===============")


