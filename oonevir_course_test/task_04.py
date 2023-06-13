from random import randint

n = 5
min_max_dict = {}
random_list = [randint(-10, 10) for i in range(n)]

print(random_list)

min_max_dict['max'] = max(random_list)
min_max_dict['min'] = min(random_list)

print(min_max_dict)
