first_set = {str(current) for current in input().split(', ')}
second_set = {str(current) for current in input().split(', ')}
if first_set != second_set and first_set.issubset(second_set):
    print(True)
else:
    print(False)