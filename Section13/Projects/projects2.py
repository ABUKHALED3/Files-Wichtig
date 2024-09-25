# open file Deep Work in mode read as f
# open or create new deep work in mode write as fout
with open('deep_work.txt') as f, open('new_deep_work','w') as fout:
    # read the file deep work und conver to upper und reverse
    data = f.read().upper() [ : : -1] 
    
    # fout write in file this data
    fout.write(data)

print(fout)