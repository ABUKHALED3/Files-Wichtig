# list of a customers
contacts = [('Mohamed Gouda', '+1-555-555-5555', 'mohamedgouda@example.com'), 
('Amira Abdelrahman', '+1-555-5555556', 'amiraabdelrahman@example.com'), 
('Abdullah Othman', '+1-555-555-5557', 'abdullahothman@example.com'), 
('Ahmed Saeed', '+1-555-555-5558', 'ahmedsaeed@example.com'), 
('Saleh Abdelhamid', '+1-555-555-5559', 'salehabdelhamid@example.com'), 
('Fatima Ali', '+1-555-555-5560', 'fatimaali@example.com'), 
('Omar Hasan', '+1-555-555-5561', 'omarhasan@example.com'), 
('Aisha Ahmed', '+1-555-555-5562', 'aishaahmed@example.com'), 
('Karim Hassan', '+1-555-555-5563', 'karimhassan@example.com')] 

# show this 
print('Contact Information')
print('*'*30)

# loop through the list of tuples and display the contact information
for contact in contacts:
    print(f'Name: {contact[0]}')
    print(f'Phone number: {contact[1]}')
    print(f'E-Mail: {contact[2]}')
    print('-'*40)