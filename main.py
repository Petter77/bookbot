import sys
from stats import count_words 
from stats import count_characters
from stats import prepare_data_for_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print("Found {} total words".format(count_words("./books/frankenstein.txt")))
    print("--------- Character Count -------")
    with open(sys.argv[1]) as f:
        text = f.read()
        char_dict: dict = count_characters(text)

        data = prepare_data_for_report(char_dict)

        for i in data:
            if i["char"].isalpha():
                print(i["char"] + ": {}".format(i["num"]))

main()
