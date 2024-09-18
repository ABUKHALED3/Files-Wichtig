
def convert_unit(number, unit ='Km'):
    if unit == 'Km':
        return f'{number * 0.6214} Miles'
    
    elif unit == 'Miles':
        return f'{number * 1.6093} Km'
    
print(convert_unit(86, unit='Km'))


