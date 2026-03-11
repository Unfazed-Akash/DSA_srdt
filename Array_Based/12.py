# Q12: Second Smallest and Second Largest Element

arr = list(map(int, input("Enter array elements (space-separated): ").split()))

unique = sorted(set(arr))

if len(unique) < 2:
    print("Not enough distinct elements")
else:
    print(f"Second smallest: {unique[1]}")
    print(f"Second largest : {unique[-2]}")
