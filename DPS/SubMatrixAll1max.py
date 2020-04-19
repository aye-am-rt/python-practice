def FindMaxSizeSubMatrix(matrix, R, C):
    if R == 0 or C == 0:
        return 0
    dp1sCountMat = [[0 for i in range(C)] for j in range(R)]
    maxNumSeen = 0
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0:
                dp1sCountMat[i][j] = matrix[i][j]
                if dp1sCountMat[i][j] > maxNumSeen:
                    maxNumSeen = dp1sCountMat[i][j]
            elif matrix[i][j] == 1:
                dp1sCountMat[i][j] = min(dp1sCountMat[i - 1][j], dp1sCountMat[i][j - 1],
                                         dp1sCountMat[i - 1][j - 1]) + 1
                if dp1sCountMat[i][j] > maxNumSeen:
                    maxNumSeen = dp1sCountMat[i][j]

    for i in range(R):
        for j in range(C):
            print(dp1sCountMat[i][j],end="  ")
        print("  ")
    return maxNumSeen


if __name__ == '__main__':
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    r = len(mat)
    c = len(mat[0])
    print(FindMaxSizeSubMatrix(mat, r, c))
