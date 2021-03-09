def rotating_numbers(n):
    s = str(n)
    digits_count = len(s)
    result = []
    result.append(int(s))
    for i in range(digits_count-1):
        s = s[-1:] + s[:-1]
        result.append(int(s))
    return result


all_numbers = rotating_numbers(12345)
print(all_numbers)
