def number_of_words(text): # Function to count number of words
    words = text.split() # Split text into words
    return len(words) # Return the count of words

def number_of_characters(text):
    ch_count = {} # Initialize empty dictionary
    for ch in text:
        ch = ch.lower() # Normalize to lowercase      
        if ch in ch_count: 
            ch_count[ch] += 1  # Increment count
        else:
            ch_count[ch] = 1 # Initialize count               
    return ch_count # Return the character count dictionary