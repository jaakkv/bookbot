#def get_book_text(filepath):
#    with open(filepath) as f:
#        content = f.read()
#        print(content)

def number_of_words(filepath):
    content = []
    with open(filepath) as f:
        content = f.read().split()
        print(f"{len(content)} words found in the document")

def main():
    number_of_words('books/frankenstein.txt')
if __name__ == '__main__':
    main()