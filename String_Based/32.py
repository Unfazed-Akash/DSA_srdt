# Q32: First Unique Character in a String
# Return the index of the first non-repeating character

from collections import Counter

s = input("Enter a string: ")
freq = Counter(s)

index = -1
for i, ch in enumerate(s):
    if freq[ch] == 1:
        index = i
        break

if index != -1:
    print(f"First unique character: '{s[index]}' at index {index}")
else:
    print("No unique character found")
