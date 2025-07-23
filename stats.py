def number_of_words(filepath):
    content = []
    with open(filepath) as f:
        content = f.read().split()
        return f"{len(content)} words found in the document"