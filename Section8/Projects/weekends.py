# lists of countries und thier weekends
countries_fri_sat = ["Egypt","Saudi Arabia","Kuwait"]
countries_sat_sun = ["USA","UAE","Germany","Australia","Switzerland"]

# input das land
das_land = input("Enter country name: ").strip()

# check das land
if das_land in countries_fri_sat:
    print(f"Freitag und Samstag sind die Wochenende in {das_land.title()}")
elif das_land in countries_sat_sun:
    print(f"Samstag und Sonntag sind die wochenende in {das_land.title()}")
else:
    print("Sorry, I don't know! ")