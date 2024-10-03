from collections import Counter

# def function to read any files txt
def read_txt_files(file_name): 
    """Get the file name txt und read the data into the file 
        paramater:
        file_name>>> file name txt
        return: 
        data_read>>> when read the data into the file 
    """
    with open(file_name) as f:
        data_read = f.read()
        return data_read.split()
    
def count_words_txt(data_file):
    """"Get the file name or any strings to count the words 

        paramters: 
        data_file>>> string data

        return: 
        count_words>>> is int"""
    count_words = 0

    for word in data_file:
        count_words += len(word)

    return count_words


def count_letter_txt(data_file):
    """" Get the file data or any strings to count letters only, not repeated
        
        paramters: 
        data_file>>> any strings
        
        return:
        count_letters>>> is int"""
    
    count_letters = 0
    for word in data_file:
        for letter in word.lower():
            if letter.isalpha():
                count_letters +=1

    return count_letters


# read the data file use function read_txt_files
data_file = read_txt_files('books_summaries_2.txt')


# count words in data use function count_words_txt
count_words = count_words_txt(data_file)

# count letters in data use function count_letters_txt

count_letters = count_letter_txt(data_file)

messages_count = f"""Word: {count_words} 
Letters: {count_letters}"""

print(messages_count)

def sorted_words_repeated(data_file):

    """ Get the data file or srings to sorted words by repeated  

        parameters: 
        data_file>>> string data

        return:
        repeated_words >>> dict"""

    # list of repeated words
    repeated_words = {}

    # sort the words 
    for word in data_file: 
        if word.isalpha() and word not in repeated_words :
            repeated_words[word]= repeated_words.get(word ,0)+ 1

    sorted_words = sorted(repeated_words.items(), key =lambda count: count[1], reverse=True)

    return sorted_words

# call to function sorted words repeated to use it
words_rep = sorted_words_repeated(data_file)

print(words_rep)