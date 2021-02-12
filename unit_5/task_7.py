import json
with open("task_7.txt", encoding="utf-8") as f:
    str = f.readlines()
    sum = 0
    count = 0
    d= {}

    for line in str:

        list = line.split()

        margine = int(list[2])-int(list[3])
        d.update({list[0]:margine})
        if margine > 0:

            sum = sum + margine
            count+=1

print(sum/count)
d.update({"average_profit":sum/count})

list=[d]
print(list)
f = open("task_5.json", "w", encoding="utf-8")
data_for_file = [list]
f.writelines(str(data_for_file))
f.close()
with open("task_7.json", encoding="utf-8") as f:
    data = f.readlines()

    print(data)