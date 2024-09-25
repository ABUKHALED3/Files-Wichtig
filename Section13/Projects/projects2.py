#عشان استخدمه علطول function ريحت الدماغ وعملت الكود جوه 
def file_red_rev (file_name):
    
    # open any file in mode read as f
    # open or create new files in mode write as fout
    with open(file_name) as f, open(f'new_{file_name}','w') as fout:
        
        # read the file  und convert to upper und reverse
        data = f.read().upper() [ : : -1] 
    
        # fout write in file this data
        fout.write(data)

file_red_rev('deep_work.txt')