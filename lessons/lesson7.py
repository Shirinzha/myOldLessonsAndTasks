# pizza = [
# 'first_item', 'second_item', 'third_item',
# 'fourth_item', 'fifth_item', 'sixth_item',
# 'seventh_item', 'and last_item'
# ]
# for item in pizza:        # с помощью  цикла for мы перебрали весь список pizza переместив в переменную item
#     print(f'eating {item} of pizze')






# pizza = [

# 'first_item', 'second_item', 'third_item',
# 'fourth_item', 'fifth_item', 'sixth_item',
# 'seventh_item', 'and last_item'
# ]

# enumerations = []

# for item in pizza:
#     new_item = item.split('_')[0]  #после split мы получим список [first, item] берем 0 индекс
#     enumerations.append(new_item.title())  #добавляем в конец списка new_item с верхним регистром
# print(enumerations)      # в итоге мы получаем список без слова  item и с заглавными буквами




# Дальше разберемся, как цикл for работает под капотом, а также заодно узнаем,
# что такое итератор.
# str_ = "hello"
# print(dir(str_))   #функция  dir()  выводит все атрибуты и методы данного метода или переменной   
# i = str_.__iter__()   #????
# print(i.__next__())   #метод __next__() выводит все буквы по одному
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())





# str_ = "world"
# str_ = str_.__iter__()    #
# print(next(str_))         #метод next() аналогичен дандер методу __next__()
# print(next(str_))
# print(next(str_))



# pizza = [
# 'first_item', 'second_item', 'third_item',
# 'fourth_item', 'fifth_item', 'sixth_item',
# 'seventh_item', 'and last_item'
# ]
# enumerations = []
# for item in pizza:
#     new_item = item.split('_')[0]    #с помощью метода split () убрали _ и последующие символы
#     if new_item.startswith('s'):     #если элементы в списке начинаются с буквы S то продолжай
#         continue
#     elif new_item.startswith('a'):   #если элемент в списке начинается с буквы A то выведи и останови итерацию
#         break
#     enumerations.append(new_item.title()) #переменную new_item поменстили в enumerations
# print(enumerations)





# pizza = [
# 'first_item', 'second_item', 'third_item',
# 'fourth_item', 'fifth_item', 'sixth_item',
# 'seventh_item', 'and last_item'
# ]
# enumerations = []
# for index, item in enumerate(pizza):  #метод  enumerate() получает в аргументы итерируемый объект и возвращает элемент и его индекс
#     print(f'This is index {index},and item ---{item}')
#     new_item = item.split('_')[0]
#     enumerations.append(new_item.title())
# print(enumerations)





# arr = [[1,2,3], [4,5,6], [7,8,9]]

# new_arr = []
# for x in arr:
#     for i in x:
#         if x not in new_arr:
#             new_arr.append(i)
#         else:
#             continue
# print(new_arr)  #Output: new_arr = [1,2,3,4,5,6,7,8,9]




#  цикл while Выполняет тело цикла до тех пор, пока условие цикла истинно.
# i = 0
# while i < 10:
#     i+=1
#     print("Hello")



password = "helloworld"
input_ = ""
while input_ != password:
    input_ = input("Enter your data: ")
    print(input_)



















































