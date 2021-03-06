# def ends_with_ed(name):
#     if (name[-2:] == 'ed'):
#         return True
#     else:
#         return False

def ends_with_ed(name):
    return (name[-2:] == 'ed')


if ends_with_ed("sorted") == True:
    print("Ending with 'ed' ")
else:
    print("NOOOOOOOO not ending with 'ed' ")

words = ['copy', 'sorted', 'ended']
methods = filter(lambda x: (x[-2:] == 'ed'), words)
methods = list(methods)
print(methods)
