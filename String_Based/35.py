# Q35: Longest Palindromic Substring
# Uses expand-around-center approach

def longest_palindrome(s):
    if not s:
        return ""

    start, max_len = 0, 1

    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)      # odd-length palindromes
        expand(i, i + 1)  # even-length palindromes

    return s[start:start + max_len]

s = input("Enter a string: ")
print(f"Longest palindromic substring: '{longest_palindrome(s)}'")
