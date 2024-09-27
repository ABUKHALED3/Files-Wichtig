# import re >> regex library
import re

# intro to Regex 

txt = """Name: Hamada Codezilla

Email: hamada23.codezilla@codezilla.com

Phone: 01743507569

Address: 456 Nile St, Giza, Egypt

DOB: 28/02/1985

Hamada Codezilla is a software engineer with over 10 years of

experience in the industry. He is skilled in web development,

databases, and programming languages such as Python and

JavaScript. He has worked for a variety of companies, from

small startups to large corporations.

Hamada can be reached at hamada23.codezilla@codezilla.com or

hamada_codezilla35@gmail.com or by phone at 01743507569. His

address is 456 Nile St, Giza, Egypt. He was born on February

28, 1985.

In his free time, Hamada enjoys playing Ping-Pong, reading tech

blogs, and spending time with his family."""

# method findall() return a list
# takes zwei args 
# Erste >>> الحاجة اللي بدور عليها
# Zweite >>>  ا النص اللي بدور في

find_all_hamada = re.findall('hamada',txt)
print(find_all_hamada)

print('-'*40)

#search_hamada = re.search('Hamada',txt)
#print(search_hamada)

find_all_codezilla = re.findall('codezilla', txt.lower())
print(f"{find_all_codezilla} \n")


# sub method replace 
# takes drei args
# Erste>>> الحاجة اللي عايز ابدلها 
# Zweite>>> الحاجة الجديد اللي احطها بدل الاوله
# Drittel>>> النص اللي بعمل في الكلام ده

new_txt = re.sub('codezilla', 'CODEZILLA', txt)
print(new_txt)