def msd(n):
    sum = 0
    s = str(n)
    for i in range(len(s)):
        sum = sum + int(s[i])
    return sum


print(msd(234))
print(msd(987))
