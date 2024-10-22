def main():
    path = "books/frankenstein.txt"
    word_count = get_word_count(path)
    print("Words in document:", word_count)

def get_word_count(text):
    with open(text, "r") as f:
        text = f.read()
        words = text.split()
        return len(words)
main()
