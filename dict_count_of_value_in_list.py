"""Напишите программу, которая принимает список строк и выводит количество повторений данных строк в списке.
Необходимо реализовать решение с использованием словарей."""

my_string = [str(current) for current in input().split(', ')]
my_dict = {}
for current in my_string:
    if current in my_dict:
        my_dict[current] += 1
    else:
        my_dict[current] = 1
for value in my_dict.values():
    print(value, end = " ")
    





    
