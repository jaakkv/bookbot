def number_of_words(filepath):
    content = []

    with open(filepath) as f:
        content = f.read().split()
        return f"{len(content)} words found in the document"

def number_of_characters(filepath):
    content = ""
    char_dict = {}

    with open(filepath) as f:
        content = f.read()

    for char in content:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1

    return char_dict