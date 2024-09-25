
# read the file Atomic Habits

with open('atomic_habits.txt' ,'r') as f:
    print(f.read().upper())
    rev = f [ : : -1]

print(rev)