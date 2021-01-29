import random

gen_list = (list(random.choice(range(0, 100)) for el in range(10)))
gen_count_list = []
[gen_count_list.append(gen_list[el]) if gen_list[el] >= gen_list[el + 1] else el for el in range(0, len(gen_list) - 1)]
print(gen_list)
print(gen_count_list)



