from stats import number_of_words, number_of_characters, sorted_char

def get_book_text(file_path):
    with open(file_path) as f: 
        return f.read()
    
def main():
    
    text = get_book_text("books/frankenstein.txt")
    char_count = number_of_characters(text)
    sorted_count = sorted_char(char_count)
    

    
    print("============ BOOKBOT ============")
    
    print("Analyzing book found at books/frankenstein.txt...")
        
    print("----------- Word Count ----------")
    
    print(f"Found {number_of_words(text)} total words")
       
    print("--------- Character Count -------")
        
    for ch, count in sorted_count.items():
        print(f"{ch}: {count}")
        
    print("==============END=================")
            
    
main()