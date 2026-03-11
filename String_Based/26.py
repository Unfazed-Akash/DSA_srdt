# Q26: Move All '#' Characters to the Front of the String

def move_hash_to_front(s):
    hashes = s.count('#')
    non_hash = s.replace('#', '')
    return '#' * hashes + non_hash

s = input("Enter a string: ")
result = move_hash_to_front(s)
print("Result:", result)
