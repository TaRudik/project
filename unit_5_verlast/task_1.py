f = open("task_1.1.txt", "a", encoding="utf-8")
while True:
    str = input()
    if str == '':
        break

f.writelines(str +'\n')
f.close()

