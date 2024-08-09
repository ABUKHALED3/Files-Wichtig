# lesson about enumerate function () الترقيم 

# a list of names 
names = ['Ahmed', 'Amr', 'Hesham', 'KhaLed']

# enumerate function () takes zwei arugments
# eins argument any iterabel zum >>> string , tuple , list , set , dic اجباري
# zwei argument ist >> الرقم اللي هبدا من عندو الترقيم اختياري  

# في متغير  function لما نيجي نحفظ الـ 
new_names = enumerate(names, 4)
#عشان نقدر نشوف هذا  list or tuple  يلزم تحويل هذا المتغير الي 
print(list(new_names))
# وبعد ذلك هيطر من الذكرة

print('-'*20)

for index , name in enumerate(names, 15):
    print(index, name)
