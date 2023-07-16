# def twoStacks(maxSum, a, b):
#     def fun(i, j, temp, a, b, maxSum, count):
#         if temp >= maxSum:
#             return 0
        
#         return min(
            
#         )

def update_rows(matrix, row, k):
    for i in range(row, min(row + k, len(matrix))):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

def pseudorandom_generator(matrix, current_row, current_col, current_value, k):
    n = len(matrix)
    m = len(matrix[0])

    if current_row == n:
        return current_value

    unit_type = matrix[current_row][current_col]

    if current_value == 0 and unit_type == 2:
        return -1

    if unit_type == 1:
        current_value += 1
    elif unit_type == 2:
        current_value -= 1

    if current_row + 1 < n:
        next_row = current_row + 1
        next_col_left = current_col
        next_col_right = current_col + 1

        if next_col_left < 0:
            next_col_left = 0
        if next_col_right >= m:
            next_col_right = m - 1

        if matrix[next_row][next_col_left] == 1:
            current_col = next_col_left
        elif matrix[next_row][next_col_right] == 1:
            current_col = next_col_right
        else:
            current_col = next_col_right

    max_pseudorandom = -1
    for rows_to_change in range(k + 1):
        new_matrix = [row[:] for row in matrix]  # Create a copy of the matrix to avoid modifying the original
        update_rows(new_matrix, current_row + 1, rows_to_change)
        result = pseudorandom_generator(new_matrix, current_row + 1, current_col, current_value, k)
        if result != -1:
            max_pseudorandom = max(max_pseudorandom, result)

    return max_pseudorandom

def maximum_pseudorandom_number(unitType, n, m, k):
    max_pseudorandom = -1
    for start_col in range(m):
        result = pseudorandom_generator(unitType, 0, start_col, 0, k)
        max_pseudorandom = max(max_pseudorandom, result)

    return max_pseudorandom

# ---------------------------------
