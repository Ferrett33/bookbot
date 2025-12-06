import sys

from stats import number_of_words, number_of_characters, sorted_char

def get_book_text(file_path):
    with open(file_path) as f: 
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book = sys.argv[1]
    text = get_book_text(sys.argv[1])
    char_count = number_of_characters(text)
    sorted_count = sorted_char(char_count)
    

    
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {book}...")
        
    print("----------- Word Count ----------")
    
    print(f"Found {number_of_words(text)} total words")
       
    print("--------- Character Count -------")
        
    for ch, count in sorted_count.items():
        print(f"{ch}: {count}")
        
    print("==============END=================")
    

    
main()