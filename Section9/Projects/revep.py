# get from user a eins wort
wort = input("Enter ein Wort: ")
print("-"*20)

# use function list to save this wort by chars
wort = list(wort)

# use method .revese() اعكس الحروف
wort.reverse()

# use join method  تجميع الحروف
reversed_wort = ''.join(wort)
print(reversed_wort)