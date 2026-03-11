# Q20: Rotate Array by K Positions (to the right)

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
k = int(input("Enter k (number of positions to rotate right): "))

result = rotate_array(arr, k)
print("Rotated array:", result)
