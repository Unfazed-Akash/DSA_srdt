# Q16: Kth Largest Element in an Array

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
k = int(input("Enter k: "))

if k < 1 or k > len(arr):
    print("Invalid value of k")
else:
    arr_sorted = sorted(arr, reverse=True)
    print(f"The {k}th largest element is: {arr_sorted[k - 1]}")
