def count_words(filepath):
    num = 0
    with open(filepath) as f:
        file = f.read()
        word_list = file.split()
        for word in word_list:
            num += 1
    return num
        
def main():
    print("Found {} total words".format(count_words("./books/frankenstein.txt")))
    
main()
