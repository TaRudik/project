a = [input("Введите элемент списка или наберите stop, если все элементы Вами уже набраны: ")]
if a[0]=="stop":
    print("Ввод элементов списка не начат")
else:
    element = 0
    while a[element] != "stop":
        a.append(input("Введите элемент списка или наберите stop, если все элементы Вами уже набраны: "))
        element += 1
    a.pop(len(a) - 1)
i = 0
while i<int(len(a)-1):
    if len(a) % 2 != 0:
        while i != (len(a) - 1):
            a.insert(i, a[i + 1])
            a.pop(i + 2)
            i += 2
        print(a)
    else:
        while i < (len(a) - 1):
            a.insert(i, a[i + 1])
            a.pop(i + 2)
            i += 2
        print(a)