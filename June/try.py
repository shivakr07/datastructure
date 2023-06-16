def convert_and_sort(N):
    char_map = {
        '1': 'A','2': 'B','3': 'C','4': 'D','5': 'E','6': 'F','7': 'G','8': 'H','9': 'I'
    }

    digits = [char_map[digit] for digit in str(N)]
    sorted_chars = sorted(digits)
    S = ''.join(sorted_chars)

    return S


N = int(input("Enter a number with digits between 1 and 9: "))
result = convert_and_sort(N)
print("Resultant string:", result)
def calculate_diagonal_sum(m, n, a, b):
    def convert_to_square_matrix(matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Convert matrix to square if it's not already
        if rows != cols:
            max_dim = max(rows, cols)
            square_matrix = [[matrix[i][j] if i < rows and j < cols else 1 for j in range(max_dim)] for i in range(max_dim)]
        else:
            square_matrix = matrix

        return square_matrix

    # Convert input arrays to matrices
    matrix1 = [a[i * n: (i + 1) * n] for i in range(m)]
    matrix2 = [b[i * n: (i + 1) * n] for i in range(m)]

    # Convert matrices to square matrices
    square_matrix1 = convert_to_square_matrix(matrix1)
    square_matrix2 = convert_to_square_matrix(matrix2)

    # Calculate diagonal sums
    diagonal_sum1 = sum(square_matrix1[i][i] for i in range(len(square_matrix1)))
    diagonal_sum2 = sum(square_matrix2[i][i] for i in range(len(square_matrix2)))

    return diagonal_sum1, diagonal_sum2
