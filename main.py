from stats import get_num_words
from stats import get_num_characters

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    num_characters = get_num_characters(book)
    print(f"Found {num_words} total words")
    print(num_characters)


def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        file_contents = f.read()
	
    return file_contents


main()
