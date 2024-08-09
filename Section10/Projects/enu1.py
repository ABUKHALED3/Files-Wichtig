# a list of tuples 
countries_and_capitals = [ 
    ("Afghanistan", "Kabul"), 
    ("Albania", "Tirana"), 
    ("Algeria", "Algiers"), 
    ("Andorra", "Andorra la Vella"), 
    ("Angola", "Luanda"), 
    ("Antigua and Barbuda", "Saint John's"), 
    ("Argentina", "Buenos Aires"), 
    ("Armenia", "Yerevan"), 
    ("Australia", "Canberra"), 
    ("Austria", "Vienna"), 
    ("Azerbaijan", "Baku"), 
    ("Bahamas", "Nassau"), 
    ("Bahrain", "Manama"), 
    ("Bangladesh", "Dhaka")]

# Print countries and capitals like this:  
 
#1. Afghanistan: Kabul 
#2. Albania: Tirana 
#3. Algeria: Algiers

# use for loop عشان الف جو 
# use enumerate function () عشان الترقيم 

for index , (country , capital) in enumerate(countries_and_capitals, 1):
    print(f'{index}. {country}: {capital}')