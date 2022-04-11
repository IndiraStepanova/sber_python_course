"""Даны два списка чисел. Напишите программу, которая определяет, сколько в них встречается общих чисел, используя множества."""
first_set = {str(current) for current in input().split(', ')}
second_set = {str(current) for current in input().split(', ')}
print(len(first_set.intersection(second_set)))
