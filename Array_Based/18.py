# Q18: Find Duplicate Number
# Find the duplicate number in an array of n+1 integers where each value is in [1, n]

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    # Phase 1: detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: find entry point of cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
print(f"Duplicate number: {find_duplicate(arr)}")
