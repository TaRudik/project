

with open('list_workers_salaries.txt') as f:
    str = f.readlines()

    i = 0
    j = 0
    sum = 0
    line_count = 0
    for line in str:
        salary = []
        name = []
        line_count += 1
        for el in line:
            j += 1
            if el.isdigit() or el == ".":
                salary.append(el)
                i += 1
            else:
                name.append(el)
                surname = ''.join(name)
                i += 1
        num = float("".join(salary))
        sum += num
        if num <= 20000:
            print(f"{surname}")
    x = round(sum / line_count, 2)
    print(f"Средняя зарплата на предприятии: {x}")


