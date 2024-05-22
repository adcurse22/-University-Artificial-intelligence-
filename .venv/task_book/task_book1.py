# num = int(input('Write a number from 1 to 9: '))
# imdex = 1
# if num < 1 or num > 9:
#     print('something went wrong')
# else:
#     for i in range(num+1):
#         print(f"{imdex} * {num} = {imdex * num}")
#         imdex += 1
#
#
# for i in range(300,430+1):
#     if i % 11 == 0 and i % 5 != 0:
#         print(i)
#
# def is_leap_year(year):
#     if year % 4 == 0 and year % 100 != 0:
#         print("leap year")
#     else:
#         print('this year is not leap year')
#
# is_leap_year(2023)
#
#
#
# def calculator(a,b,type):
#     if type=='+':
#         return a+b
#     elif type=='-':
#         return a-b
#     elif type=='*':
#         return a*b
#     elif type=='/':
#         return a/b
#
# print(calculator(1,2,'+'))
#
# dollar = 77.4
# gallon = 15.8
# gallon_price = 3.89
# lst = [2790, 820, 6*110,gallon/gallon_price]
# total_sum = []
# for i in lst:
#     total_sum.append(i*dollar)
#
# print(round(sum(total_sum)))
# print(lst)
# for i in lst:
#     if i in alp:
#         print(i,end='-')
#     elif i == ' ':
#
#
# Получаем ввод пользователя
words = input("Введите три слова через пробел: ")

# Разбиваем введенную строку на отдельные слова
word_list = words.split()

# Создаем новый список для хранения преобразованных слов
transformed_words = []

# Проходимся по каждому слову в списке
for word in word_list:
    # Преобразуем каждую букву в заглавную и добавляем дефисы между буквами
    transformed_word = '-'.join(word.upper())
    # Добавляем преобразованное слово в список
    transformed_words.append(transformed_word)


alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

lst = 'Вставай на лыжи'

# Выводим преобразованные слова через пробел
print(' '.join(transformed_words))


new_lst = lst.upper()
for i in new_lst:
    if i == '':
        print(f"{i}-", end='-')
    else:
        print(i,end='-')

def duplicate_count(text):
    count = 0
    for i in set(text):  # Проходимся по уникальным символам в строке
        if text.count(i) > 1:  # Проверяем, сколько раз символ встречается в строке
            count += 1
    return count

# Пример использования
print(duplicate_count("hello"))  # Должно вывести: 2, так как "l" встречается дважды

