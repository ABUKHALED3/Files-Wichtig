books =  {'Buch1': 'atomic_habits.txt',
          'Buch2': 'deep_work.txt',
          'Buch3': 'dopamine_nation.txt',
          'Buch4': 'power_habit.txt',
          'Buch5': "so_good_they_can't.txt",
          'Buch6': 'tasting_tee.txt'
          }

# read all books und add all txt in file 

def read_book (file_name):

    with open(file_name,'w') as f:
        # read the book 
        data = f.read()
        return data