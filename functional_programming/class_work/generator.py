def generator(val):
    while val > 0:
        yield val
        val = val - 1


gen_iter = generator(5)
print(gen_iter)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
