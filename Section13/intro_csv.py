# import library csv
import csv

# def a function to read csv file
def read_csv_file(file_name):
    """ Get file name
        Read the data the from file 
    Return the data in the file as a list"""

    # open the file
    with open(file_name) as f:
        
        # Read the File Emplpoyees Data
        # use method reader () return object
        file_data = csv.reader(f)

        # convert object to list 
        # عشان اقدر اشوف البيانات 
        file_data_lst = list(file_data)

        return file_data_lst
    
# def a function to  Double the salary of each Employee 
def update_salary(employees_lst):

    # use for loop through csv_data_lst
    for employee in employees_lst:
        
        # replace , to empty 
        #float  عشان اقدر احول الرقم الي 
        employee[-1] = employee[-1].replace(',','')

        # float قبل الضرب نحولها الي 
        #اضربها في 2 list  أخر قيمة في الـ 
        employee[-1] =  float(employee[-1]) * 2
    
    return employees_lst

# def function 
#def employess_salary (salary):
    # رتب علي اساس
    # salary [-1] الاول
    #شبه بعضه salary في تطابق و الـ 

    #salary[0] رتب علي اساس الـ 
    # في تطابق بردو 

    #salary[1] رتب علي اساس الـ 
    #return  float(salary [-1]) , salary[0] , salary[1]

def sort_salary(update_employees_lst):
    sorted_employess = sorted (update_employees_lst, key= lambda salary : (salary[-1], salary[0], salary[1]))
    return sorted_employess

# Write employess data to a file
def write_csv_file(file_name, new_data):
    # open or create a new file --- mode>>> write und save it in variable new_file
    with open(file_name, 'w', newline='') as new_file:
        # use method writer 
        # عشان اقدر اكتب في الملف ده وخزنتها في متغير
        new_data_emps = csv.writer(new_file)

        # use method writerows () takes list
        #new_data هكتب في الـ 
        #sorted_employees اللي هكتبو هنا في 
        new_data_emps.writerows(new_data)


def main():
    # read the data
    # call to function read csv file und save it data in a file
    csv_data_lst = read_csv_file('employees_data.csv')
        
    #update the salary
    # call to function update salary
    updated_employees = update_salary(csv_data_lst)

    # sort the salary
    # call to function sort salary
    sorted_employees = sort_salary(updated_employees)

    # write the data into new file
    # call to function write csv file
    write_csv_file('new_emps_data', sorted_employees)

    print('Done (Fertig)')

# الموبايل باظ و بحاول اصلحه بقالي 3 ساعات

if __name__ == '__main__':
    main()




