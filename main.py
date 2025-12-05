from stats import number_of_words

def get_book_text(path):
    with open(path) as p:
        return p.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words(text)

main()