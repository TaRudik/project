def my_func(a, b):
        return 1/(a **(b))
print(my_func(a=int(input("Введите первое число : ")), b= - int(input("Введите отрицательное число : "))))

##
def my_func_2(x, y):
    d=1
    while y<0:
        d=d*x
        y+=1
    return 1/d
print(my_func_2(x=int(input("Введите первое число : ")), y=int(input("Введите второе число : "))))