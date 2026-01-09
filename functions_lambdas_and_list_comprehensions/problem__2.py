words = ["hi", "python", "is", "cool", "code", "a"]


def filter_words(words):
    is_long = lambda word : len(word) > 3
    long_words = [word for word in words if is_long(word)]

    return long_words


long_words = filter_words(words)
print(f"List of long words: {long_words}")