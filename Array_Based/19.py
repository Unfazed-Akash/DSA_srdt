# Q19: Merge Two Sorted Arrays

def merge_sorted(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

arr1 = list(map(int, input("Enter first sorted array (space-separated): ").split()))
arr2 = list(map(int, input("Enter second sorted array (space-separated): ").split()))

result = merge_sorted(arr1, arr2)
print("Merged sorted array:", result)
