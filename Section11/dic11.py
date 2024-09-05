# lesson fur dic use method get

txt = """Welcome to codezilla course we are happy to have you
all here hope you enjoy the course"""

# create a empty dic
letter_count = {}

# use for loop though txt
for letter in txt:
    # letter شوف كده هل عندك 
    # key und value 0 لا ضيف الـ 
    letter_count[letter] = letter_count.get(letter, 0)
    #key 1 زود قيمة الـ 
    letter_count[letter] += 1

print(letter_count)