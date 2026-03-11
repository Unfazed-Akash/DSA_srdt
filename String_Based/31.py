# Q31: Check if Two Strings are Valid Anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print(f'"{s1}" and "{s2}" are anagrams')
else:
    print(f'"{s1}" and "{s2}" are NOT anagrams')
