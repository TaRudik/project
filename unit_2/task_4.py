a = input("Введите строку: ")
b = a.split()
i = 0
for ind, el in enumerate(b, 1):
    if len(str(b[i])) <= 10:
        print(ind, el)
        i = i + 1
    else:
        print(ind, b[i][0:10])
        i = i + 1
