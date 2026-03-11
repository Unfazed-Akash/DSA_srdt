# Q10: Count Occurrences of an Integer in a List

lst = list(map(int, input("Enter list elements (space-separated): ").split()))
target = int(input("Enter the integer to count: "))

count = lst.count(target)
print(f"Occurrences of {target} in the list: {count}")
