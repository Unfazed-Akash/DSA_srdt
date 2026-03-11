# Q3: Maximum Marks per Semester
# Accept the number of students, their total marks,
# and calculate max marks per semester (6 semesters total)

SEMESTERS = 6

n = int(input("Enter the number of students: "))

for i in range(1, n + 1):
    total_marks = float(input(f"Enter total marks of student {i}: "))
    max_per_semester = total_marks / SEMESTERS
    print(f"Student {i}: Maximum marks per semester = {max_per_semester:.2f}")
