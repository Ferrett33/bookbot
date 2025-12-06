from stats import number_of_words, number_of_characters

def get_book_text(file_path):
    with open(file_path) as f: 
        return f.read()
    
def main():
    text = get_book_text("books/frankenstein.txt") 
    
    words = number_of_words(text)
    print(f"Found {words} total words.")
    char_count = number_of_characters(text)
    print(char_count)

main()