called_times = 0


def sum_of_numbers(nums):
    global called_times
    called_times += 1
    # 1. terminating cond
    if len(nums) == 1:
        return nums[0]

    # 2. breaking the problem into smaller parts
    n = len(nums)
    first_half = nums[:n//2]
    second_half = nums[n//2:]

    # 3. call the recursive with sub-problems
    sum_half_1 = sum_of_numbers(first_half)
    sum_half_2 = sum_of_numbers(second_half)

    # 4. combine the solution
    res = sum_half_1 + sum_half_2
    return res


print(sum_of_numbers([5, 6, 1, 2]))
print(called_times)
