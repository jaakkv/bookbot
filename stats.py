def number_of_words(filepath):
    content = []

    with open(filepath) as f:
        content = f.read().split()
        return f"Found {len(content)} total words"

def number_of_characters(filepath):
    content = ""
    char_dict = {}

    with open(filepath) as f:
        content = f.read()

    for char in content:
        if char.isalpha():
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1

    result = [{"char": c, "num": n} for c, n in char_dict.items()]
    return result

def sort_dictionary(list):
    return list["num"]


