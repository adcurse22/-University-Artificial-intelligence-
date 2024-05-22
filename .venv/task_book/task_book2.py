
import numpy as np
import matplotlib.pyplot as plt
import random
# tensor = np.random.randint(5,10,(1,2,3))    # Во вторых скобках заданы размеры тензора в высоту, ширину, глубину (оси X,Y,Z)
# print(tensor)
# print('Количество осей: ',tensor.ndim)
# print('Форма массива: ',tensor.shape)
# print('Количество значений: ',tensor.size)

# matrix = np.random.randint(-10, 10, (5, 5))     # Значения матрицы случайны в пределах (-10, 10), 5 строк и 5 столбцов
# print(matrix)


# print(matrix[:,1])

# my_array = np.random.randint(-5, 10, (3,3))   # Создание массива
# print(my_array)
#
# print("Максимум всех элементов по первой оси: ", my_array.max(axis=0))
# print(end=' ')
# print("Минимум всех элементов по первой оси: ", my_array.min(axis=0))
#
# print("Максимум всех элементов по первой оси: ", my_array.max(axis=1))
# print(end=' ')
# print("Минимум всех элементов по первой оси: ", my_array.min(axis=1))
#

# x = np.linspace(0, 15, 101)
#
# # Вот какой массив х получился в итоге:
# print(x)
# y = np.sin(x)
#
# plt.figure(figsize=(10, 5))                   # Задание размера полотна в дюймах
#
# plt.plot(x, y, label='sin(x)')                # Параметр label задает подпись кривой
# plt.plot(x, np.cos(x)/2, label='cos(x)/2')    # Отрисовка еще одного графика на полотне
#
# plt.title("y = sin(x)")                       # Заголовок графика
# plt.xlabel('Переменная X')                    # Надпись для оси x
# plt.ylabel('Переменная Y')                    # Надпись для оси y
#
# plt.grid()                                    # И только здесь новое - команда grid(), чтобы отрисовать сетку на фоне
#
# plt.show()



#
# first_vector = np.zeros(5,dtype=int)
# second_vector = np.ones(5,dtype=int)
# third_vector = np.full(5,3)
# print(first_vector,second_vector,third_vector,sep='\n')


# list_names = ['Jake','Michael','Bob','Claire','Jimmy','Sara','Joseph','David','Franklin','Adolph']
# np_array = np.array(list_names)
# print('Тип списка имен = ',type(list_names))
# print('Тип массива имен = ',type(np_array))


# array1 = np.random.randint(1,5,size=10)
# print(array1.dtype)


# array1 = np.arange(10)
# print(array1.mean())


# array = np.random.randint(1,150,size=100)
# print(array)
# print(array[0],array[32],array[-2])

# my_array = np.random.uniform(1,16,size=(6,6))
# print(my_array)
# my_mean = my_array.mean()
# print(my_mean)

# array0 = np.zeros((7,7))             # Создание массива из нулей размером 7 на 7
# array0[3] = 1                        # Замена всех элементов 3-ей строки на 1
# array0[:,3] = 1                     # Замена всех элементов 3-го столбца на 1
# print(array0)                        # Вывод результата


# numbers = [i**3 for i in range(1, 10)]
# print(numbers)

#
# array1 = np.random.randint(1,10,10)
# array2 = np.random.randint(1,10,4)
# print(np.in1d(array1,array2))


# a = np.array([[2, 3, 4], [3, 2, 1]])
# b = np.array([[7, 8], [5, 6], [3, 4]])
#
# b = b.reshape(2, 3)
# print(b)                                    # Преобразование массива b к размерности 2х3
# c = a + b                           # Сложение массивов
# print(c.sum())                      # Вывод суммы всех элементов
#
# array1  = np.random.randint(1,20,20)
# print(array1)
# array2 = array1[0:10]
# array2.sort()
# print(array2)
# array3 = array1[10:20]
# array3.sort()
# print(f'{array2},{array3}')

# a = np.random.randint(0, 100, (6, 8))       # Создание массива из числовых элементов
# b = np.array(a, dtype='U10')                # Создание массива с теми же значениями, но из текстовых элементов
# b[a > 50] = 'пан'                           # Замена элементов на соответствующие условию
# b[a <= 50] = 'пропал'
# print(b)


# a = np.random.randint(0,10,30)
# print(a)                             # Вывод массива
# print(np.bincount(a).argmax())

# array1 = np.array([0, 10, 20, 40, 60])
# array2 = [10, 30, 40]
#
# for i in array1:
#     for j in array2:
#         if i == j:
#             print(i)

# print(np.intersect1d(array1, array2))


# chess_array = np.zeros((8,8), dtype=int)        # Создание нулевого массива
# chess_array[1::2,::2] = 1                       # Заполнение четных строк
# chess_array[::2,1::2] = 1                       # Заполнение нечетных строк
# print(chess_array)


# equal = np.allclose(A, B)           # Получение массива сравнения
# print(equal)
#
# array = np.arange(100)
# needed_num = np.random.uniform(0,100)
#
# index = np.abs(array-needed_num).argmin()
# print(array-needed_num)
# print(needed_num,index)



# x = np.random.randint(0, 9, 5)          # Создание первого произвольного вектора
# y = np.random.randint(0, 9, 5)          # Создание второго произвольного вектора
# plt.plot(x, y)                          # Создание графика
# plt.xlabel('x')                         # Подпись оси x
# plt.ylabel('y')                         # Подпись оси y
# plt.show()

# plt.plot(x, y,marker= 'o')                          # Создание графика
# plt.xlabel('x')                         # Подпись оси x
# plt.ylabel('y')
# plt.title('График функций')
#
# plt.show()


# x = np.random.randint(0, 5, 10)                     # Создание первого случайного вектора
# y = np.random.randint(0, 5, 10)                     # Создание второго случайного вектора
# plt.xlabel('x')                                     # Подпись оси х
# plt.ylabel('y')                                     # Подпись оси y
# plt.plot(x, y, color='blue', linestyle='dotted')    # Первый график
# plt.plot(y, x, color='red', linestyle='dashed')     # Второй график
# plt.title("Двойной график")                         # Подпись графика.
# plt.show()

# Создайте четыре вектора x1, x2, x3, x4 с данными типа float и один вектор y типа int, размерность каждого массива - 10 элементов. Отобразите все 4 графика на одном полотне разными цветами.
# x1 = np.random.rand(10)
# x2 = np.random.rand(10)
# x3 = np.random.rand(10)
# x4 = np.random.rand(10)
# y = np.random.randint(0, 100,10)          # Создание значений оси у
# plt.plot(x1, y)                            # Первый график
# plt.plot(x2, y)                            # Второй график
# plt.plot(x3, y)                            # Третий график
# plt.plot(x4, y)                            # Четвертый график
# plt.show()

#Постройте горизонтальную гистограмму, опрелеляющую зависимость числа учеников в классе по росту. Первый список содержит рост учеников, второй список - количество учеников заданного роста.
# height = [130, 135, 140, 145, 150, 155]           # Список ростов
# num = [2, 6, 9, 8, 7, 1]                          # Список количества учеников
# x_pos = [i for i, _ in enumerate(height)]         # Перебор ростов
# plt.barh(x_pos, num, color='green')               # Построение горизонтальной гистограммы
# plt.xlabel("Количество")                          # Подпись оси х
# plt.ylabel("Рост")                                # Подпись оси у
# plt.title("Рост/количество учеников")             # Подпись графика
# plt.yticks(x_pos, height)                         # Значения на оси у
# plt.show()

# height = [130, 135, 140, 145, 150, 155]           # Список ростов
# num = [2, 6, 9, 8, 7, 1]
#
#
#
# fig1, ax1 = plt.subplots()
#
# print(fig1,ax1)
# ax1.pie(num, labels=height, autopct='%1.1f%%')
# plt.show()

# x = np.random.randn(1,105)
# print(x)
# y = np.random.randn(1,105)
# plt.scatter(x,y)
# plt.show()

#HOME WORK LITE UII

# array1 = np.arange(1,11)
# array2 = np.arange(1,5)
# x = np.in1d(array1,array2)
# print(x)


#
# def cartesian_to_polar(x, y):
#     # Вычисляем полярный радиус
#     r = np.sqrt(x  2 + y  2)
#
#     # Вычисляем полярный угол
#     if x > 0:
#         theta = np.arctan(y / x)
#     elif x < 0:
#         theta = np.arctan(y / x) + np.pi
#     else:  # x == 0
#         if y > 0:
#             theta = np.pi / 2
#         elif y < 0:
#             theta = -np.pi / 2
#         else:  # y == 0
#             theta = 0
#
#     return (theta, r)

#
# # Пример использования:
# x = 4
# y = 3
# polar_coords = cartesian_to_polar(x, y)
# print("Декартовы координаты (x, y):", (x, y))
# print("Полярные координаты (угол, радиус):", polar_coords)


# chess_array[1::2,::2] = 1
# chess_array[::2,1::2] = 1
# my_array = np.zeros((7,7),dtype=int)
# n = 0
# while n <= 6:
#   my_array[n][n] = 1
#   my_array[n][-n-1] = 1
#   my_array[n][3] = 1
#   my_array[3][n] = 1


#   n += 1
#
# plt.imshow(my_array)
# plt.show()
#
#
# programmingLanguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
#
# popularity = [10,40,5,30,10,25]
#
# colors = ["red", "blue", "green", "yellow", "orange", "brown"]
#
# plt.pie(popularity, labels=programmingLanguages, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.show()
#
#
# x1 = np.linspace(-100,100)
# y1 = x1 ** 3 / 100
# y2 = x1 ** 2
# plt.ylabel("Y-LABEL")
# plt.xlabel("X-LABEL")
# plt.plot(x1, y1, color='blue', linestyle='dashed',label='x^3/100')    # Первый график
# plt.plot(x1, y2, color='orange', linestyle='dashed',label='x^2')
# plt.legend(fontsize=14)
#
# plt.title('Function Values')
# plt.show()