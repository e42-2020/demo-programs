def square(n):
    res = n*n
    return res


def cube(m):
    res = m * square(m)
    return res


print(square(4))
print(cube(2))
