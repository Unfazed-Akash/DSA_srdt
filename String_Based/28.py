# Q28: Counting Valleys
# A valley is a sequence of steps below sea level starting with a downward step
# and ending with an upward step that returns to sea level.
# Input: a string of 'U' (up) and 'D' (down) steps

def counting_valleys(path):
    level = 0
    valleys = 0
    for step in path.upper():
        if step == 'U':
            level += 1
            if level == 0:      # just returned to sea level from below
                valleys += 1
        elif step == 'D':
            level -= 1
    return valleys

path = input("Enter the hiking path (U/D steps, e.g. UDDDUDUU): ")
print(f"Number of valleys: {counting_valleys(path)}")
