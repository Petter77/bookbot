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

def sort_on(items: dict):
    return items["num"]

def prepare_data_for_report(items: dict):
    result = []
    for item in items:
        result.append({"char":item, "num":items[item]})

    result.sort(reverse=True, key=sort_on)
    return result

