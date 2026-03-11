# Q14: Matrix Identity Check
# Check if a given square matrix is an identity matrix

def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
            if i != j and matrix[i][j] != 0:
                return False
    return True

n = int(input("Enter the size of the square matrix (N): "))
matrix = []
print("Enter matrix elements row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

if is_identity(matrix):
    print("The matrix is an Identity Matrix")
else:
    print("The matrix is NOT an Identity Matrix")
