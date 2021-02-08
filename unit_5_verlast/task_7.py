import json
with open("task_7.txt", encoding="utf-8") as f:
    str = f.readlines()
    sum = 0
    count = 0
    data = {}

    for line in str:

        list = line.split()

        margine = int(list[2])-int(list[3])
        data.update({list[0]:margine})
        if margine > 0:

            sum = sum + margine
            count+=1

print(sum/count)
data.update({"average_profit":sum/count})

list = data
print(list)
with open("task_7.json", "w", encoding="utf-8") as write_f:
        json.dump(data, write_f)
