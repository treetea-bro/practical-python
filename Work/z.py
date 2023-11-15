w = [[1, 2, 3, 4]]


def a(w):
    for i in w:
        yield i


print(id(w[0]))
print(id(next(a(w))))
