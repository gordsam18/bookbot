from stats import (
    get_num_words,
    get_num_characters, 
    sort_dict
)

def main():
    get_report()


def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        file_contents = f.read()
	
    return file_contents

def get_report():
    
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    num_characters = get_num_characters(book)
    chars_sorted_list = sort_dict(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()
