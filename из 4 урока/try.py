from itertools import count



def fact():
    for el in count(1):
        
        yield el


num = fact()
x = 0
for i in num:
    if x < 15:

        x += 1
        print(i)
    else:
        break
