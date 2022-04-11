'''Задан список с числами. Напишите программу, которая выводит все элементы списка, которые больше предыдущего, 
в виде отдельного списка.'''
input_list = [int(current) for current in input().split()]
output_list = []
previous = input_list[0]
for current in input_list[1:]:
    if current > previous:
        output_list.append(current)
        previous = current
    else:
        previous = current
print(*output_list)        
