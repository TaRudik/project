revenue = int(input("Введите выручку Вашей компании в у.е.: "))
costs = int(input("Введите издержки Вашей компании в у.е.: "))
if revenue > costs:
    print(f"Компания работает с прибылью: {revenue - costs} у.е.")
    profitability = round(((revenue - costs)*100/revenue), 2)
    print(f"Компания работает с рентабельностью: {profitability} %")
    number_wokers = int(input("Введите число сотрудников  Вашей компании: "))
    print(f"Компания работает с прибылью в пересчете на одного работника: {round((revenue - costs)/number_wokers, 2)} у.е.")
else:
    print("Компания не имеет прибыли или работает в убыток")
