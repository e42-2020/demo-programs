def ninna(n):
    print("ninna:", n)
    monna(n-1)
    print("ninna:", n)


def monna(n):
    if n <= 0:
        return
    print("monna:", n)
    ninna(n-1)
    print("monna:", n)


ninna(5)
