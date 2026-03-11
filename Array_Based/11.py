# Q11: Spiral Matrix Traversal
# Traverse and print all elements of a matrix in spiral order

def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements row by row:")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

print("\nSpiral order traversal:")
print(spiral_order(matrix))
