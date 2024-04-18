def sort_on(dict):
    return dict['count']

def convert_dict_to_sorted_list(dict):
    new_list = []

    for i in dict:
        item = {"character": i, "count": dict[i]}
        new_list.append(item)
    
    new_list.sort(reverse=True, key=sort_on)
    
    return new_list

def get_letter_count(contents):
    contents = contents.lower()
    letters = {}
    
    for letter in contents:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    
    return letters
    
def get_word_count(contents):
    words = contents.split()
    return len(words)
    
def get_book_path(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        raise Exception("Sorry an error occurred. Please ensure you've entered a valid file path to a valid file type.")
        
def main():
    book_path = input("Please enter the file path to your book: ")
    
    if not book_path:
        raise Exception("ERROR: Please enter the file path to your book.")
    
    book_text = get_book_path(book_path)
    num_words = get_word_count(book_text)
    num_chars = get_letter_count(book_text)
    char_counts = convert_dict_to_sorted_list(num_chars)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
        
    for char in char_counts:
        print(f"The '{char['character']}' character was found {char['count']} times.")
    
    print("--- End report ---") 
    
main()