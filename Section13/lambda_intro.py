# Die Lektion für lambda function 

menu =[['Das Wasser', 12],
       ['Der Kaffee', 25],
       ['Der Tee', 20],
       ['Die Milch mit Datteln', 30]
       ]

# lambda function 
#defبطريقة  function دي بدل ما تعرفه 
#بسيط خالص function  ونستخدمها عند عمل 

#lambda شرح 

#1. args و بكتب هتاخد كام  lambda  بكتب 
#2. retrun (menu[1] , menu[0]) لو هرجع اكتر من قيمة لازم احطهم جو أقواس
# return  طريقة الـ 
sorted_menu = sorted(menu , key= lambda menu : (menu[1], menu[0]))

print(sorted_menu)
