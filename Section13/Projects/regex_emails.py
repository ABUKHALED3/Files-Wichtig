import re

# open file emails with open save a file into variable named f
with open('emails.txt') as f:
    # use method read() to read the file und save it in dataf
    dataf = f.read()

# das ist mein pattern
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

email_pattern2 = r'[\w.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z]+'

email = re.findall(email_pattern, dataf)


print(email)
