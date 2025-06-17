def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_num_characters
from stats import sort_char_counts

def main():
    
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        word_count = f"Found {num_words} total words"
        character_count = get_num_characters(book_text)
        sorted_count = sort_char_counts(character_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(word_count)
        print("--------- Character Count -------")
        for current_dictionary in sorted_count:
            print(f"{current_dictionary['char']}: {current_dictionary['num']}")
        print("============= END ===============")

main()