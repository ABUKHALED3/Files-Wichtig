# 1. multiplication table in the following format: 
 
# 1 x 1 = 1 
 
# 1 x 2 = 2 
 
# ........

# creat a counter
counter = 1

# loop 1 to 10 for each table like table 1, table 2,  etc.
for i in range (1 , 11):
        
        # loop 1 to 10
        for j in range(1, 11):
                # الضرب بقا من 1 لحد 10 
                # i في قيمة الـ 
                product = i * j

                # print the product in the format of 1 x 1 = 1
                print(f'{i} x {j} = {product}')
        
        # print a line 
        print('-'*30)