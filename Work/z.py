z = [y for x in [1, 2, 3] for y in [x, 10 * x]]

print(z)

a = []
for x in [1, 2, 3]:
    for y in [x, 10 * x]:
        a.append(y)

print(a)

q = [[1], [2], [3], [4, 5]]

print([j for i in q for j in i])
