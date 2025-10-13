def count_words(filepath):
    num = 0
    with open(filepath) as f:
        file = f.read()
        word_list = file.split()
        for word in word_list:
            num += 1
    return num
        
def count_characters(text):
    text = text.lower()
    dictionary = {
        
    }
    
    for character in text:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    return dictionary
