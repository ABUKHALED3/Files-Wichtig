list_of_numbers = [1 ,4 ,6 ,7 ,9 ,5 ,7 ,3 ,2 ,4]

def convert_list_to_any(args, convert_to_int=False, convert_to_float=False, convert_to_str=False):
    result = []
    
    for i in args:
        if convert_to_int:
            result.append(int(i))

        
        elif convert_to_float:
            result.append(float(i))
            
        elif convert_to_str:
            result.append(str(i))
            
        else:
            result.append(i)

    return result


print(convert_list_to_any(list_of_numbers))