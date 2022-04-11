""" 1. Задан словарь. Напишите программу, которая будет выводить значение по заданному ключу.
2. Напишите программу, которая будет выполнять действие, обратное заданию 1. 
Программа должна производить поиск по значению и выдавать ключ."""

some_dict = {1 : 'a', 2 : 'b', 3 : 4, 'd' : 4, 'e' : 5}
input_key = str(input()) #возвращение значение по введеному ключу
for key, value in some_dict.items():
    if input_key == str(key):
        print(value)

"""input_value = str(input()) #возвращение ключа по введеному значению
for key, value in some_dict.items():
    if input_value == str(value):
        print(key)"""

 