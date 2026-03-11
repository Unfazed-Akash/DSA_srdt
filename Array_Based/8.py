# Q8: Matrix Rotation by 90 Degrees (Clockwise)
# Rotate an N x N matrix 90 degrees clockwise in-place

def rotate_90_clockwise(matrix):
    n = len(matrix)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

def print_matrix(matrix):
    for row in matrix:
        print(row)

n = int(input("Enter the size of the square matrix (N): "))
matrix = []
print("Enter matrix elements row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

print("\nOriginal Matrix:")
print_matrix(matrix)

rotate_90_clockwise(matrix)

print("\nMatrix after 90-degree clockwise rotation:")
print_matrix(matrix)
