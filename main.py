def main():
    path = "books/frankenstein.txt"
    word_count, word_list = get_word_count(path)
    print("Words in document:", word_count)

    character_counts = get_char_counts(word_list)
    print("Character counts in document:", character_counts)

def get_word_count(text):
    with open(text, "r") as f:
        text = f.read()
        words = text.split()
        return len(words), words

def get_char_counts(words):
    characters = {}

    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

    return characters

main()
