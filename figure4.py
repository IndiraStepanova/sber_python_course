x=int(input())
for i in range(x):
    print(" " * x, sep = "", end = "")
    for j in range(i, 0, -1):
        print(j, sep = "", end = "")
    print()
for i in range(x, 0, -1):
    print(" " * x, sep = "", end = "")
    for j in range(i, 0, -1):
        print(j, sep = "", end = "")
    print()