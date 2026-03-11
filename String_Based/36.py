# Q36: Longest Common Prefix

def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

n = int(input("Enter number of strings: "))
words = [input(f"String {i + 1}: ") for i in range(n)]

result = longest_common_prefix(words)
print(f"Longest common prefix: '{result}'" if result else "No common prefix")
