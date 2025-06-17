def get_num_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def get_num_characters(book_text):
    chars = book_text.lower()
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_char_counts(char_count):
    sorted_count = []
    for character, count in char_count.items():
        if character.isalpha():
            current_char_count = {"char" : character, "num" : count}
            sorted_count.append(current_char_count)
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count
