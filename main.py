def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()

def number_of_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")
    return len(words)    

