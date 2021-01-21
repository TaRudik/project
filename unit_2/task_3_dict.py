my_dict = {'зима': [12, 1, 2],
           'осень': [9, 10, 11],
           'весна': [3, 4, 5],
           'лето': [6, 7, 8]}
spring = my_dict.get('весна')
winter = my_dict.get('зима')
autome = my_dict.get('осень')
summer = my_dict.get('лето')
number = int(input("Введите номер месяца: "))
while number >= 0:
    if 1 <= number <= 12:
        for j in range(0, 3):
            if number == spring[j]:
                print("весна")
            elif number == winter[j]:
                print('зима')
            elif number == autome[j]:
                print('осень')
            elif number == summer[j]:
                print('лето')
        break
    else:
        number = int(input("В году 12 месяце попробуйте ввести число от 1 до 12. Введите номер месяца: "))

