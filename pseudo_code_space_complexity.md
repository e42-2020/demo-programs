## Pseudo code for two ways of computing maximum of n numbers.
```
n = read_number()
Read n numbers into an array 'numbers'
# Process the array 'numbers' and find the max.
max = numbers[0]
i = 1
while i < n:
	if max < numbers[i]:
		max = numbers[i]
	i = i + 1
print(max)
```
O(n + 4) space needed. ~ O(n) space complexity.

- - - -
```
n = read_number()
max = read_number()
n = n - 1
while n > 0:
	next_number = read_number()
	if max < next_number:
		max = next_number
	n = n -1
print(max)
```
O(3) is space needed. ~ O(1) Space complexity
