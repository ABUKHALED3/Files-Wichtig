strings = ['apple', 'banana', 'pear', 'orange'] 

def filter_strings(strings_list,str):
  return [string for string in strings_list if str in string ]
    




print(filter_strings(strings,'p'))
        