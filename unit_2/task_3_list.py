my_list = [[12, 1, 2], [9, 10, 11],
           [3, 4, 5], [6, 7, 8]]
number = int(input("Введите номер месяца: "))
winter = my_list[0]
autome = my_list[1]
spring = my_list[2]
summer = my_list[3]
i = 0
if number in range(1,13):
    for el in spring:
        if spring[i] == number:
            print("spring")
            break
        else:
            i += 1
    if summer[0]== number or summer[1]== number or summer[2]  == number:
        print("summer")
    j = 0
    for el in winter:
        if winter[j] == number:
            print("winter")
            break
        else:
            j += 1
    if autome[0] == number or autome[1] == number or autome[2] == number:
        print("autome")

else:
    print("В году 12 месяцев")

