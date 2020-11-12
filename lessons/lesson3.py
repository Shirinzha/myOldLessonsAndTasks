# #тип данных: списки(элементы)   
# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda']
# print(cars[2])
# print(cars[-1])
# print(cars[0][-1]) #пайтон читает сверху вниз, слева на право
# #индексы пишутся в квадратных скобках,  только если надо сделать срез
# # можно сделать двойной срез
# print(cars[2].upper())
# print('я хотел бы купить себе новую машину')

# cars[-1] = 'porshe' 
# print(cars)
# #пишем индекс, присваиваем, заменяем


# #методы списков
# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda']
# cars.append('mustang') #метод  append  добаляет новый элемент в конец
# print(cars) 

# cars1 = [] # пустой список
# cars1.append('mazda')
# print(cars1)

# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda']
# cars.insert(2, 'masserati')
# print(cars)
# # метод инсерт добавляет новый элемент в произвольную позицию в списке через указание индекса


# del cars[4] # удаление элемента из списка через индекс
# print(cars)


# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda']
# popped_cars = cars.pop() #новая переменная присваивается
# print(cars) 
# print(popped_cars) #метод поппед удаляет с конца элемент, но позволяет работать с ним после удаления. если указать индекс то он удалит этот элемент



# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda' , 'toyota']
# print(cars)
# cars.remove('toyota')
# print(cars) #удаление элемента из списка через значение. если не знаем индекс то можно так. один ремув удаляет толькко одно значение


# alpha = ['s', 'd' , 'e' , 'p' , 'b' , 'a' , 'g']
# print(alpha)
# alpha.sort()
# alpha.sort(reverse=True)
# print(alpha) #метод сорт сортирует буквы и числа по порядку, а если добавить аргумент ресерв то отсортирует в обратном порядке


# alpha = ['s', 'd' , 'e' , 'p' , 'b' , 'a' , 'g']
# print(sorted(alpha, reserve=True)) #функция сортед сортирует временно

# alpha = ['s', 'd' , 'e' , 'p' , 'b' , 'a' , 'g' , 'A' , 'G' , 'C' , 'B']
# print(sorted(alpha))
# alpha.reverse()
# print(alpha)
# len(alpha)
# print(len(alpha))



# # работа со списками. переменные со списками должны вводится во множественном числе
# cars = ['audi' , 'toyota' , 'bmw' , 'mercedes' ,'mazda' , 'toyota'] 
# for car in cars: #в случае for ставится двоеточие
#     print('у меня есть машина'+ car.title())
#     print('у меня нет машины ')    
# #итерация- это перебор элементов в нашем обьекте(список). есть итерируемые и не итерируемые элементы. цикл работает до тех пор пока перебираемые элементы закончатся.
# #табуляция- отступ внутри кода(четыре пробела или tab)

# # создание списков через генератор чисел
# #первый вариант
# numbers = []
# for number in range(2, 20): # старт энд и степ #функция рэйндж для генерации чисел
#     numbers.append(number)
#     print(numbers)

# # второй вариант
# new_numbers = list(range(0,20))
# print('result', new_numbers)


# squares = []
# for num in range(1,15):
#     square = num**2
#     squares.append(square)
# print(squares)
# # нашли квадрат каждого числа 

# squares = []
# for num in range(1,15):
#     squares.append(num**2)
# print(squares)


# numbers = [1,2,3,4,5,6,7,8,9,10]
# # max функция находит самое большое число внутри списка
# # min функция находит самое маленькое число внутри списка
# # sum находит сумму всех чисел
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))



min max append insert popped 
6.переменная х=1 до 20 с помощбю цикла 
y=1
for x in range(1,10):



print(numbers.index(3))# находит индекс значения внутри списка


x = [1]*10
print(x)













