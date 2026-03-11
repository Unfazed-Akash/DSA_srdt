# Q22: Count Pairs with Given Sum

def count_pairs(arr, target):
    count = 0
    freq = {}
    for num in arr:
        complement = target - num
        count += freq.get(complement, 0)
        freq[num] = freq.get(num, 0) + 1
    return count

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
target = int(input("Enter the target sum: "))

print(f"Number of pairs with sum {target}: {count_pairs(arr, target)}")
