# Q33: Find the First Non-Repeated Character in a String

def first_non_repeated(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

s = input("Enter a string: ")
result = first_non_repeated(s)

if result:
    print(f"First non-repeated character: '{result}'")
else:
    print("All characters are repeated")
