def sum_num():
    sum = 0
    a = True
    while a == True:
        b = input("Введите числа через пробел: ").split()
        for i in range(len(b)):
            if b[len(b) - 1] == "stop":
                for i in range(len(b)):
                    if b[i] != "stop":
                        sum = sum + int(b[i])
                    elif b[i] == "stop" and len(b) - 1 != i:
                        sum = sum
                    else:
                        a = False
                        return (sum)
                        break

            elif b[i] == "stop" and b[len(b) - 1] != b[i]:
                sum = sum
            else:
                sum = sum + int(b[i])
        print(f"Сумма числе равна = {sum}")

    return (sum)


print(f"Итоговая сумма всех введенных чисел равна = {sum_num()}")
