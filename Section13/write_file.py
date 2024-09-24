#عشان افتح الملف وانسه اقفله open  بدل ما استخدم 
#fافضل وهو بيقفل الملف لوحده وهنا اختصارت الملف في متغير اسمه  with استخدم 
#with open('employess_data.txt') as f:

# هفتح الملف ده في وضع الكتابة لكن خالي بالك من الوضع ده عشان بيحذف اللي موجود 
#with open('employess_new_data.txt','w') as f:

#append الحل اني افتح الملف في 
with open('employess_new_data.txt','a') as f:
    f.write('ich lerne pythonkurs')
    f.write('Hallo\n')




    