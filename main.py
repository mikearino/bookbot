

def get_book_text(path):
    with open(path) as p:
        return p.read()

def number_or_words(input):
    count = 0
    words = input.split()
    for word in words:
        count += 1
    print(f"Found {count} total words")

def main():
    text = get_book_text("books/frankenstein.txt")
    number_or_words(text)

main()