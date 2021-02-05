a = [7, 5, 5, 3, 3, 2]
copy_a = a.copy()
copy_a.reverse()
i = 0
d = []
n = input("Введите число, если хотите начать заполнять рейтинг или stop, если хотите закончить запонение рейтинга:")
while n != "stop":
    d = []
    n = int(n)
    i = 0
    while i < len(a) - 1:
        if a[len(a) - 1] >= n:
            copy_a.reverse()
            d.extend(copy_a)
            d.append(n)
            a = d
            copy_a = a.copy()
            copy_a.reverse()
            n = input("Введите число, если хотите начать заполнять рейтинг или stop, если хотите закончить запонение рейтинга:")
            break
        elif n < a[i]:
            if a[i] == a[i + 1]:
                d.append(a[i])
                copy_a.pop()
                i += 1
            else:
                d.append(a[i])
                copy_a.pop()
                i += 1
        elif n == a[i]:
            if a[i] == a[i + 1]:
                d.append(a[i])
                copy_a.pop()
                i += 1
            else:
                d.append(a[i])
                copy_a.reverse()
                d.extend(copy_a)
                a = d
                copy_a = a.copy()
                copy_a.reverse()
                n = input("Введите число, если хотите начать заполнять рейтинг или stop, если хотите закончить запонение рейтинга:")
                break
        elif n >= a[i]:
            if n >= a[i] or a[i] != d[i]:
                d.append(n)
                copy_a.reverse()
                d.extend(copy_a)
            a = d
            copy_a = a.copy()
            copy_a.reverse()
            n = input("Введите число, если хотите начать заполнять рейтинг или stop, если хотите закончить запонение рейтинга:")
            break
print(a)

