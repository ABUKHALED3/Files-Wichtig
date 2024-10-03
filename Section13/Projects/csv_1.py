
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
        return data_read
    
data_file = read_txt_files('books_summaries_2.txt')


def count_words_txt(data_file):

    count_words = 0

    for word in data_file.split():
        count_words += len(word)

    return count_words


count_words = count_words_txt(data_file)

print(count_words)