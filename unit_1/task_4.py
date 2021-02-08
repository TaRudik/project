number = tuple(input("Введите целое положительное число: "))
i = 0
b = 9 #переменная пробегающая от 9 до 0 с шагом 1
while b <= 9:
    if int(number[i]) == b:
        print(f'Наибольшая цифра в введенном Вами числе равна: {number[i]}.')
        break
    if int(number[i]) < b and i < len(number)-1:
        i += 1
    else:
        b -= 1
        i = 0

