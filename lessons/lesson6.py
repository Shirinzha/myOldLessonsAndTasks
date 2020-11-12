# dict1 = {'key':'value', 'key2':'value2', 'key3':'value3'}

# for key, value in dict1.items(): #метод items дает возможность перебрать наш словарь с ключом и значением
#     print('key:', key)
#     print('value:', value)






# dict2 = {'python': 'kanym', 'java':'shirin', 'js':'nursultan'}    
# for key, value in dict2.items():
#     print(value + 'изучает' + key.upper() + '.')





# dict2 = {'python': 'kanym', 'java':'shirin', 'js':'nursultan'} 
# languages = []
# users = []

# for key, value in dict2.items():
#     print(value + 'изучает' + key.upper() + '.')
#     languages.append(key)
#     users.append(value)
# print(languages)    
# print(users)




# name1 = input('first name ')
# name2 = input('second name ')
# name3 = input('third name ')

# dict2 = {'python': name1, 'java':name2, 'js':name3} 
# languages = []
# users = []
# for key, value in dict2.items():
#     print(value.title() + ' learns ' + key.upper())
#     languages.append(key)
#     users.append(value.title())
# print(languages)
# print(users)



# dict2 = {'python': 'kanym', 'java':'shirin', 'js':'nursultan'} 

# for key in dict2.keys():   #этот метод дает возможность перебирать в цикле все ключи из словаря
#     print('our squad knows' + key)
#     if key.lower() == 'python':
#         print('who is ', dict2[key]) #принт выдает нам значение ключа 






# dict2 = {'python': 'kanym', 'java':'shirin', 'js':'nursultan'} 

# for key in dict2.keys(): 
#     print('our squad knows ' + key)
#     print(dict2[key])





# dict2 = {'python': 'kanym', 'java':'shirin', 'js':'nursultan'} 

# for value in dict2.values():
#     if value.lower() == 'nursultan':
#         dict2['js'] = 'nina'
# print(dict2)

# for value in dict2.values():
#     print(value)





# user_dict = {'id':123124, 'age':15, 'address':'osmonova 55'}
# users_list = []
# for user_number in range(20):
#     user_dict['number'] = user_number   #добавили новое значение
#     users_list.append(user_dict)        #добавили в список
# print(users_list)

# for user in users_list:         # перебираем список с 20 списками
#     print(user['id'])           # принтует значение ключа 20 раз




company = {'name':'ithub' ,
 'address':'furmanova' ,
  'phone':'0999134494' , 'staff': ['sultan','zarema','einar']}
for name in company['staff']:     # обращаемся к ключу и берем список и перебираем в цикле помещая в переменной name
    print(name.title())




















