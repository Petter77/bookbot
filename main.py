from stats import count_words 
from stats import count_characters


def main():
    print("Found {} total words".format(count_words("./books/frankenstein.txt")))
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        char_dict = (count_characters(text))
        print(char_dict)

main()
