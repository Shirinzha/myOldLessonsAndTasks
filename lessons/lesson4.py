# #кортеж- неизменяемый тип данных(список). для него нет методов. можно использовать фор. можно читать но не менять.

# # неизменяемые типы данных
# x = 90
# print(id(x))
# x = 91
# print(id(x)) #id  не изменился а перезаписался


# list1 = [1,2,3,4,5]
# print(id(list1))
# print(list1)
# list1.append(6) # тут идет не перезапись всего списка, а добавили один элемент(перезапись) 
# print(id(list1)) #а айди не меняется
# print(list1)


# #КОМАНДЫ IF (условие) в конце ставится двоеточие и пишется с табуляцией после. в пайтон тру и фолсе пишутся с заглавой буквы
# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda'] 
# for car in cars:
#     if car == 'bmw': #if всегда ожидает труе. == оператор сравнивания
#         print('моя любимая машина-это' + car.upper())
#     else: 
#         print('это не mercedes')
#        #else используем в том случае если иф не срабатывается




# password = input(' пожалуйста введите ваш пароль:  ') 
# if password != 'qwerty':    #! в случае неравенства используется этот оператор
#     print(' неправильно')
# else:
#     print('добро пожаловать')    


# age = input('enter your age')
# if int(age) >=18:
#     print('welcome')
# else:
#     print('you cannot enter')


# age1 = 17
# age2 = 16
# if age1>=18 and age2>=16:
#     print('welcome')
# else:
#     print('nope')


# age1 = 17
# age2 = 16
# if age1>=18 or age2>=16:
#     print('welcome')
# else:
#     print('nope')



# baned_users=['askar','bermet','shirin','kanym','sultan','nursultan']
# user = 'mirlan'
# if user in baned_users:
#     print('welcome'+ user)
# else:
#     print('you cant')


# baned_users=['askar','bermet','shirin','kanym','sultan','nursultan']
# user = 'askar'
# if user not in baned_users:
#     print('welcome'+ user)
# else:
#     print('you cant')

#    # not оператор отрицание, который переводит true и false в другие состояния
#    # оператор in проверяет на присутствие одного элемента в другом 


# text='abc'
# if 'a' in text:
#     print('yes')
# else:
#     print('no')


# marriedstatus = True
# if marriedstatus:
#     print('married')
# else:
#     print('not')

# status = input('enter 1 if you are a student, enter 0 if you are not: ')
# if status=='1':
#     studentstatus= True
# else:
#     studentstatus= False
# if studentstatus:
#     print('student')        
# else:
#     print('not student')




# status = input('enter 1 if you are a student, enter 0 if you are not: ')

# if status=='1':
#     studentstatus= True 

# elif status=='0': #else + if = elif это дополнительная проверка
#     print('error')
#     #в этой последовательности условий может работать только одно условие

# if studentstatus:
#     print('student')        
# else:
#     print('not student')



# empty_list=[]
# list2=[1,2,34]
# if empty_list:
#     print('список не пустой')
# else:
#     print('список пустой')


  1  задание перевести все в секунды и интежер
2 фор и иф


# if x.isupper():
#   print('malenkie')
# elif x.islower():
#   print('bolshie')
проверка на тру фолсе


x = 'a'
z = 0
y = 0
if x.islower():
  
