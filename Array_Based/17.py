# Q17: Missing Number
# Find the missing number in an array containing 0 to n (one number missing)

arr = list(map(int, input("Enter array elements (space-separated, range 0 to n with one missing): ").split()))

n = len(arr)  # array has n elements, so full range is 0..n
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

print(f"Missing number: {expected_sum - actual_sum}")
