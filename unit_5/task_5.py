f = open("task_5.txt", "w", encoding="utf-8")
data_for_file = [input(str())]
f.writelines(data_for_file)
f.close()
with open("task_5.txt", encoding="utf-8") as f:
    data = f.readlines()
    new_data = data[0].split(" ")
    sum=0
    for el in new_data:
        sum=sum+int(el)
    print(sum)

