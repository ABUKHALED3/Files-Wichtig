contacts = [('Mohamed Gouda', '+1-555-555-5555', 'mohamedgouda@example.com'), 
('Amira Abdelrahman', '+1-555-5555556', 'amiraabdelrahman@example.com'), 
('Abdullah Othman', '+1-555-555-5557', 'abdullahothman@example.com'), 
('Ahmed Saeed', '+1-555-555-5558', 'ahmedsaeed@example.com'), 
('Saleh Abdelhamid', '+1-555-555-5559', 'salehabdelhamid@example.com'), 
('Fatima Ali', '+1-555-555-5560', 'fatimaali@example.com'), 
('Omar Hasan', '+1-555-555-5561', 'omarhasan@example.com'), 
('Aisha Ahmed', '+1-555-555-5562', 'aishaahmed@example.com'), 
('Karim Hassan', '+1-555-555-5563', 'karimhassan@example.com')] 


while True:

    # Display the menu
    print('Welcome to the phonebook application!')
    print('1. Add a contact')
    print('2. Update a contact')
    print('3. Search for a contact')
    print('4. Quit')

    # Get the user's Choice
    user_input = int(input('Enter Your Choice: '))

    # Add a contact
    if user_input == 1 :
        name  = input('Enter a name: ')
        phone = input('Enter Phone number: ')
        email = input('Enter email: ')
        #list of tuples  هنضيف ده كلو في الـ 
        contacts.append((name, phone, email))

    # Update Contact 
    elif user_input == 2:
        name = input('Enter name of the contact you want to update: ')

        # for loop throug list tuples
        for i in range(len(contacts)):
            if contacts[i][0].lower() == name.lower():
                phone = input('Enter new phone number: ')
                email = input('Enter new email: ')
                contacts[i] = (name, phone, email)
                print('Contact update successfully')
                break
        else:
            print('Contact not found')

    # search for a contact
    elif user_input == 3:
        name = input('Enter name of the contact you want to search: ')
        for contact in contacts:
            if contact[0].lower() == name.lower():
                print(f'Name: {contact[0]}')
                print(f'Phone number {contact[1]}')
                print(f'Email: {contact[2]}')
                break
        else:
            print('Contact not found')
    
    # Quit 
    elif user_input == 4:
        break

    # Invalid user input
    else:
        print('Invalid user input')
    
    print('-'*20)

