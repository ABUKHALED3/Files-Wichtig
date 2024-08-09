# a list 
sentences = ['Hello from Codezilla', 'Python Course is awesome', 
'I enjoy learning Python with Codezilla'] 

# use for loop عشان اللف جو und use enumerate function ()  عشان الترقيم
# loop through in list of sentences
for index , word in enumerate(sentences):
     #  اشوف كل مسافة ابدلها بي - وكل الحروف كبير
     sentences[index] = word.upper().replace(' ', '-')

# print when for loop ist False
print(sentences)