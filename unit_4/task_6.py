
from itertools import count, cycle


num = []
for el in count(3):
    if el > 10:
        break
    else:
        num.append(el)
print(num)



list = [5, 'g', 7,'y']
iter_str = cycle(list)
new_list = []
while len(new_list)<40:
    new_list.append(next(iter_str))
print(new_list)