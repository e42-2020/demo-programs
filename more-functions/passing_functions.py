def show(functions):
    functions[2](x, y)
    functions[0](x, y)
    functions[1](x, y)
    functions[3](x, y)


def add(a, b):
    res = a+b
    print(res)


def sub(a, b):
    res = a-b
    print(res)


def mul(a, b):
    res = a*b
    print(res)


x = 2
y = 3
function = [sub, mul, add, None]
show(function)
