# list of Salaries
salaries = [13544, 54554, 44541, 44546, 54447, 54817,
            54471, 15134, 44401, 10257, 15047,  24547,
            41545, 21252, 47104, 14155, 12354, 14245,
            54024, 40425, 25042, 54567, 54040, 45405,
            11227, 16542, 12375, 20487, 65122, 15241,
             ]

# list of Salaries made in ChatGpt
salaries_chatgpt = [8500, 11200, 6700, 13400, 9800, 14300, 
                    10100, 5600, 12900, 7300, 15000, 4900, 
                    10800, 7900, 11600, 13700, 9100, 10500, 
                    8200, 12100, 6900, 13200, 15700, 14004,
                    ]

# use method .copy() to copy values in this list 
all_salaries = salaries.copy() 
# use mehtod .extend() to add a values in this list
all_salaries.extend(salaries_chatgpt)

# use a sort method to sort this list (reverse=True) من الكبير الي الصغير عند تغير الي
sorted_salaires = all_salaries [:]
sorted_salaires.sort(reverse=True)

# max salary
max_salary = max(sorted_salaires)
print(f"The Max Salary in Firma ist {max_salary:,}")

# min salary
min_salary = min(sorted_salaires)
print(f"The Min Salary in Firma ist {min_salary:,}")

# average salary
# sum of sorted_salaries / lenth of sorted_salaries 
avg = sum(sorted_salaires) / len(sorted_salaires)
print(f"The Average salary in Firma ist {avg:,.0f}")

# highest 5 salaries 
print(f"The Highest 5 Salary in Firma ist {sorted_salaires[:5]}")

# lowest 5 salaries
print(f"The Lowest Salary in Firma ist {sorted_salaires[-5:]}")
