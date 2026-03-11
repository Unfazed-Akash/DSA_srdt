# Q29: String Compression (Run-Length Encoding)
# "aaabbbcc" -> "a3b3c2"
# If compressed string is not shorter, return original

def compress_string(s):
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    result = ''.join(compressed)
    return result if len(result) < len(s) else s

s = input("Enter a string: ")
print("Compressed string:", compress_string(s))
