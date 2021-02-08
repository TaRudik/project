with open('list_workers_salaries.txt') as f:
    str = f.readlines()
    i = 0
    j = 0
    line_count = 0
    for line in str:
        word = 0
        j += 1
        line_count += 1
        for el in line:
            if el != " " and el != "\n" :
                i += 1
            elif el == " " or el == '\n':
                i = 0
                word += 1


        if j == len(str):

            print(f"В последней строке: {word + 1}")
        else:
            print(f"{line_count} строка: {word}")
print(f"В документе {line_count} строк")

