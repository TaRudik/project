with open("task_7.txt", encoding="utf-8") as f:
    str = f.readlines()
    sum = 0
    count = 0
    d=dict()
    print(d)
    for line in str:

        list = line.split()

        margine = int(list[2])-int(list[3])
        d = dict("list[1]" = 'margine')
        if margine > 0:
            print(margine)
            sum = sum + margine
            count+=1

print(sum/count)
