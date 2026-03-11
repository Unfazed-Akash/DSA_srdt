# Q34: Check if a String is a Palindrome

s = input("Enter a string: ")
cleaned = s.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')
