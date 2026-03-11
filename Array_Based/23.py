# Q23: Move Zeros to End (maintain order of non-zero elements)

def move_zeros(arr):
    pos = 0
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
move_zeros(arr)
print("Array after moving zeros to end:", arr)
