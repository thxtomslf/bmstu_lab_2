def get_column(B, idx):
    column = []
    for row in B:
        column.append(row[idx])
    return column


def row_column_multiplication(row, column):
    res = 0
    row_len = len(row)
    for i in range(row_len):
        res = res + row[i] * column[i]
    return res


def matrix_multiplication(A, B):
    C = []
    try:
        if any(map(lambda x: len(x) != len(B), A)) or any(map(lambda x: len(x) != len(A), B)):
            raise ValueError("Incorrect matrix sizes")
        for row in A:
            column_number = len(B[0])
            c_row = []
            for column_idx in range(column_number):
                column = get_column(B, column_idx)
                c_row.append(row_column_multiplication(row, column))
            C.append(c_row)
        return C
    except ValueError as err:
        return err.args[0]


def print_matrix_modified(matrix):

    for ind_of_row in range(len(matrix)):
        row_str = ""
        for ind_of_col in range(len(matrix[ind_of_row])):
            indent = max(map(lambda x: len(str(x)), (elem[ind_of_col] for elem in matrix[0:len(matrix)])))
            row_str = row_str + str(matrix[ind_of_row][ind_of_col]).rjust(indent) + "  "
        print(row_str)


a = [[123, 3312122, 1, 1231312113], [122, 3, 3333, 11111111111111], [11111, 1, 1, 1], [1, 231, 1312, 111]]
print_matrix_modified(a)  # Выравниваем по наибольшему в столбце элементу
