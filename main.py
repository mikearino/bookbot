def get_book_text(path):
    with open(path) as p:
        return p.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()