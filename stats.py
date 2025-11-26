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

def sort_on(items):
    return items["num"]

def sort_dict(my_dict):
    my_list = []
    for x in my_dict:
        my_list.append({"char": x, "num": my_dict[x]})
    my_list.sort(reverse=True, key=sort_on)
    return my_list


    
