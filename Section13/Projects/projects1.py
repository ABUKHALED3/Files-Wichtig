
# open the file atomic_habits in read mode
# open or creat a file name new_output on write mode 
with open('atomic_habits.txt') as f, open('new_output.txt','w') as fout:

    # use method read to read a file und conver to upper und save it varaible data
    data = f.read().upper()
    # عكس البيانات 
    data_reversd = data[ : : -1]

    # كتبت في الملف الجديد البيانات 
    fout.write(data_reversd)





