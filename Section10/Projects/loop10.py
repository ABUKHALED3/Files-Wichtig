# قمت بنشاء متغير لحفظ في قيمة 1
count = 1 

# متغير لحفظ مجموع الأرقام
total = 0 

# محتاج أكرر العملية دي  مرة 2000 while loop استخدام 
while count <= 2000:
    
    #هل الرقم ده يقبل القسمة علي 3 و 7 
    if count % 3 == 0 and count % 7 == 0:
        
    # total اجمع الرقم علي القيمة اللي موجوده في 
        total += count

    # زود بواحد
    count += 1

# when while loop >>> False 
print('Total is',total)
