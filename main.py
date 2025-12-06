def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

from stats import number_of_words

def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words(text)

main()
