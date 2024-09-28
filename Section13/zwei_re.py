# import re >> regex library
import re

txt = """Name:Hamada Codezilla

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

# هاتلي اي رقم عندك هنا
match_nums = re.findall(r"\d+", txt)
print(match_nums)

print('-'*40)

# دور علي الأرقام متكونه من 11 رقم
match_phones = re.findall(r'\d{11}',txt)
print(match_phones)

# extract the name 
match_name = re.findall(r'Name:(.+)',txt)
name = match_name[0]
print(name)

# extract the email
email_pattern = r'Email: (\S+)'
email_match = re.findall(email_pattern, txt)
email = email_match[0]
print(email)

# extract der Geburtstag The date of birth
dob_pattern = r'DOB: (\d{2})/(\d{2})/(\d{4})'
dop_match = re.findall(dob_pattern, txt)
dop = dop_match[0]

# day Tag
print(dop[0])

# month Monat
print(dop[1])

# year Jahr
print(dop[2])