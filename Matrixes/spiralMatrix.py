# Tried but was not able to do correctly
# took some help only in this question otherwise rest were piece of cake :)


def print_spiral_matrix(m, n, a):
    row_start = column_start = 0
    while row_start < m and column_start < n:
        for i in range(column_start, n):
            print(a[row_start][i], end=" ")
        row_start += 1
        for i in range(row_start, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        if row_start < m:
            for i in range(n - 1, (column_start - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        if column_start < n:
            for i in range(m - 1, row_start - 1, -1):
                print(a[i][column_start], end=" ")
            column_start += 1


if __name__ == '__main__':
    # r, c = input("give row and column for matrix").strip(" ").split(" ")
    # matrix = [[int(input("give a number ")) for i in range(int(c))] for j in range(int(r))]
    # print(str(matrix))
    myMat = [[91, 29, 38, 46],
             [54, 65, 73, 58],
             [95, 10, 11, 12],
             [13, 14, 15, 16]]
    r, c = 4, 4
    print("matrix in spiral form == ")
    print_spiral_matrix(int(r), int(c), myMat)
