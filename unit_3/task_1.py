def div(num1, num2):
    if num2 == 0:
        print("Второе число не должно равняться нулю.")
        num2 = int(input("Введите второе число повторно: "))
    else:
        result = num1/num2
    return num1 / num2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Результат деления равен: {div(a,b)}")

##

def div(num1, num2):
    if num2 == 0:
        print("Второе число не должно равняться нулю.")
        num2 = int(input("Введите второе число повторно: "))
    else:
        result = num1/num2
    return num1 / num2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Результат деления равен: {div(a,b)}")