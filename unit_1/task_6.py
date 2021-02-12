km_first = [int(input("Количество км в 1 день: "))]
km_goal = [int(input("Введите целевое количество км: "))]
days = [1]
i = 0
while km_goal[i] >= km_first[i]:
    days.append(days[i] + 1)
    km_first.append(km_first[i] * 1.1)
    km_goal.append(km_goal[0])
    i += 1
print(f"На {days[i]} день спортсмен достиг результата не менее {km_goal[i]} км.")
