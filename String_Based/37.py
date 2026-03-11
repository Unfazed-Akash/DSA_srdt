# Q37: String Rotation Check
# Check if s2 is a rotation of s1
# e.g., "abcde" rotated -> "cdeab"

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_rotation(s1, s2):
    print(f'"{s2}" IS a rotation of "{s1}"')
else:
    print(f'"{s2}" is NOT a rotation of "{s1}"')
