def middle_digit(n):                # n = 763
    num_string = str(n)             # num_string = '763'
    digits = list(num_string)       # ['7', '6', '3']
    middle_pos = len(digits)//2     # 3//2 = 1
    digit_str = digits[middle_pos]  # '6'
    result = int(digit_str)
    return result


print(middle_digit(12345))
