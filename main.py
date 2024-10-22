def main():
    path = "books/frankenstein.txt"
    word_count, word_list = get_word_count(path)

    character_counts = get_char_counts(word_list)

    generate_report(word_count, character_counts, path)

def get_word_count(text):
    with open(text, "r") as f:
        text = f.read()
        words = text.split()
        return len(words), words

def get_char_counts(words):
    characters = {}

    for word in words:
        for letter in word:
            if not letter.isalpha():
                continue
            letter = letter.lower()
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

    return characters

def generate_report(word_count, char_counts, document):
    print(f"--- Begin report of {document} ---\n")
    print(f"{word_count} words found in the document\n")

    for char in char_counts:
        print(f"The '{char}' character was found {char_counts[char]} times")

    print("--- End report ---")
main()
