# Q25: Intersection of Two Arrays (unique common elements)

arr1 = list(map(int, input("Enter first array (space-separated): ").split()))
arr2 = list(map(int, input("Enter second array (space-separated): ").split()))

intersection = sorted(set(arr1) & set(arr2))
print("Intersection:", intersection)
