names = ['hai', 'hello', 23.56]
ages = [1, 2, 3, 5]
res = zip(names, ages)
for item in res:
    print(item)

print(list(res))
