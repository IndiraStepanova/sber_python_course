'''Задан список с числами. Напишите программу, которая выводит все элементы списка с четными индексами в виде нового списка.'''

input_list = [int(current) for current in input().split()]
output_list = []
for i in range(len(input_list)):
    if i % 2 == 0:
        output_list.append(input_list[i])
print(*output_list)
