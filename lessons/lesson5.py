#СЛОВАРИ все что находится в фигурных скобках это словари. это один из типов данных. 
# вся взаимосвязанная информация хранится в словаре
# у словарей в качестве ключа может быть  только строка, после ключа ставится двоеточие и значение(можно присвоить переменную, список)
# {'key':'value', 'key1':'value'}
# у словарей в качестве ключа может быть только строка
# ключ всегда должен быть уникальным(название ключа не должно повторяться)

# car = {'color':'black','made':'toyota','year':1996, 'owner':'askar ali'}
# print(car['year'], car['color'])
# print('i have a car with color' + car['color'].upper())




# alien_0 = {'color':'green', 'points':5}
# print(alien_0)

# #добавление новых пар в словарь. в квадратных скобках пишем ключ и равно значение
# alien_0['xposition']=0
# print(alien_0)

# alien_0['yposition']=5
# print(alien_0)

# #пустой словарь
# alien_1 = {}

# alien_0 = {'color':'green', 'points':5}
# alien_0['color']= 'red'    #изменение значений в словаре(пишем ключ и даем новое значение)
# print(alien_0)





# alien_0 = {'xposition':0, 'yposition':25, 'speed':'slow'}

# if alien_0['speed']=='medium':
#     x_increment = 5
# elif alien_0['speed']=='slow':
#     x_increment = 2
# else:
#     x_increment = 10

# alien_0['xposition'] = alien_0['xposition'] + x_increment # сокращенный alien_0['xposition'] += x_increment

# print(alien_0)             
# 
# вся взаимосвязанная информация хранится в словаре




# x = 0
# for num in range(1,10):
#     x += num
#     x -= num
#     x *= num
#     x /= num
#     x **= num
# print(x)    


# alien_0 = {'xposition':0, 'yposition':25, 'speed':'slow', 'fly':'high'}
# del alien_0['fly']
# print(alien_0)












