from itertools import count

def fact():
    for el in count(1):
        yield el


num = fact()
x = 0
list = []
for i in num:
    if x < 15:
        x += 1
        list.append(i)

    else:
        break

k = 1
for el in list:
    k = list[el - 1] * k
print(k)