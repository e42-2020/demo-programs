def add():
    s = a + b
    print(s)


def increment():
    global a, b
    a = 30
    b = 90


a = 2
b = 3
add()
increment()
add()
