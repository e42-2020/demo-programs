def sum_of_numbers(nums):
    # 1. terminating cond
    if len(nums) == 1:
        return nums[0]

    # 2. breaking the problem into smaller parts
    first_part = nums[:-1]

    # 3. call the recursive with sub-problems
    sum_first_part = sum_of_numbers(first_part)

    # 4. combine the solution
    res = sum_first_part + nums[-1]
    return res


print(sum_of_numbers([12, 1, 8]))
