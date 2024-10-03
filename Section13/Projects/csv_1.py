
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


# sort the words 

repeated_words = []

#sorted_words = sorted(data_file, key = lambda word: word[0])

#print(sorted_words)
