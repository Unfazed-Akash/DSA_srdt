# Q9: Binary Search
# Search for a target element in a sorted array

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter sorted array elements (space-separated): ").split()))
target = int(input("Enter the target element to search: "))

index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")
