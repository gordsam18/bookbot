def get_num_words(book):
   return len(book.split())

def get_num_characters(book):
    lower = book.lower()
    num_characters = {}
    for character in lower:
        if character in num_characters:
            x = num_characters[character]
            x += 1
            num_characters[character] = x
        else:
            num_characters[character] = 1
    return num_characters
