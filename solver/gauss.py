# Algorytm Gaussa wzięty ze StackOverflow

def solve(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[max_row][k]
            A[max_row][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x
