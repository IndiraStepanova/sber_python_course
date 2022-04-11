'''Задан список с числами. Напишите программу, которая меняет местами наибольший и наименьший элемент 
и выводит новый список. например, входные данные: 3 4 5 2 1, выходные данные 3 4 1 2 5 - 1 и 5 меняются местами''' 
input_list = [int(current) for current in input().split()]
output_list = []
output_list = input_list.copy()
max_num = input_list.index(max(input_list))
min_num = input_list.index(min(input_list))
del output_list[max_num]
output_list.insert(max_num, min(input_list))
del output_list[min_num]
output_list.insert(min_num, max(input_list))
print(*output_list)