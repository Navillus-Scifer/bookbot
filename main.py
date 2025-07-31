import sys
from stats import word_count
from stats import character_count
from stats import sorted_count
from stats import get_book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path) 
    num_words = word_count(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    chars_dict = character_count(book_text)
    sorted_chars_list = sorted_count(chars_dict) 
    
    print("--------- Character Count -------")
    
    for item in sorted_chars_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============") # END FOOTER

if __name__ == "__main__":
    main()