from functools import reduce

lst = ['f', 'a', 't', 'h', 'e', 'r']
result = reduce(lambda a, x: a + x, range(100))
word = reduce(lambda a, x: a + x, lst)
print(result)
print(word)

