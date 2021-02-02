with open("task_4.txt", encoding="utf-8") as f:
    list = f.readlines()
n = open("task_4rus.txt", "w", encoding="utf-8")
data_for_file=[]
rus = ["Один", "Два", "Три", "Четыре"]
eng = ["One", "Two", "Three", "Four"]
for line in list:
    u = line.split(" ")

    i = 0
    for el in u:
        for words in eng:
            if el == words:
                u.insert(u.index(words), rus[i])
                u.pop(u.index(words))
                data_for_file=[" ".join(u)]
                n.writelines(data_for_file)
                i += 1
            else:
                i += 1
n.close()


