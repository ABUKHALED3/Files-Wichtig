patients = { 
"Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1}, 
"Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2}, 
"Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3}, 
"Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4} 
} 

# use while loop

while True:
    # get from user input
    # use title.() to capitalize First letter in each word 
    user_input = input('Enter the patient name (Press Enter to Exit): ').title()

    if user_input == '':
        break

    # create a variable to save age 
    # use get.() to show value 
    age = patients.get(user_input, {}).get('age', 'Not Available')

    # create a variable to save disease
    disease = patients.get(user_input, {}).get('disease', 'Not Available')

    # create a variable to save room
    room = patients.get(user_input, {}).get('room', 'Not Available')

    message = f"""Patient: {user_input}
Age: {age}
Disease: {disease}
Room: {room}
  """
    
    print(message)