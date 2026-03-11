# Q13: Merge Overlapping Intervals
# Given a list of intervals, merge all overlapping intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

n = int(input("Enter the number of intervals: "))
intervals = []
for i in range(n):
    s, e = map(int, input(f"Interval {i + 1} (start end): ").split())
    intervals.append([s, e])

result = merge_intervals(intervals)
print("\nMerged intervals:")
for interval in result:
    print(interval)
