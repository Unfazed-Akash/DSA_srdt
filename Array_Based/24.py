# Q24: Majority Element (appears more than n/2 times)
# Uses Boyer-Moore Voting Algorithm

def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
result = majority_element(arr)
print(f"Majority element: {result}")
