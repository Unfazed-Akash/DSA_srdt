# Q38: Longest Substring Without Repeating Characters
# Uses sliding window technique

def length_of_longest_substring(s):
    char_index = {}
    max_len = 0
    start = 0

    for end, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= start:
            start = char_index[ch] + 1
        char_index[ch] = end
        max_len = max(max_len, end - start + 1)

    return max_len

s = input("Enter a string: ")
result = length_of_longest_substring(s)
print(f"Length of longest substring without repeating characters: {result}")
