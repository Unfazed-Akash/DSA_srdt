# Q21: Maximum Product Subarray

def max_product_subarray(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)

    return result

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
print(f"Maximum product of a subarray: {max_product_subarray(arr)}")
