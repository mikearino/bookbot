def number_of_words(input):
    count = 0
    words = input.split()
    for word in words:
        count += 1
    print(f"Found {count} total words")