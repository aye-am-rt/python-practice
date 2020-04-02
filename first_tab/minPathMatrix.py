# Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost
# of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse
# through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including
# both source and destination). You can only traverse down, right and diagonally lower cells from a given
# cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1)
# can be traversed. You may assume that all costs are positive integers.
R = 3
C = 3


def getIndexInMatrix(myMatrix, val):
    # x, y = [(index, row.index(val)) for index, row in enumerate(myMatrix) if val in row]
    for i, j in enumerate(myMatrix):
        for k, l in enumerate(j):
            if l == val:
                print("index of mn = ", [i, k])
                return [i, k]
    return [-1, -1]


def minCost(costsMatrix, m, n):
    if m > R or n > C:
        return -1
    if m < 0 or n < 0:
        return -1
    tc = costsMatrix[0][0]
    xc = yc = 0
    for i in range(m):
        for j in range(n):
            if i == xc and j == yc:
                mn = min(costsMatrix[i][j + 1], costsMatrix[i + 1][j], costsMatrix[i + 1][j + 1])
                print(f"i={i} and j={j} and mn={mn}")
                tc += mn
                xc, yc = getIndexInMatrix(costsMatrix, mn)
            # print(f"i={i} and j={j} and cmij={costsMatrix[i][j]}")
    return tc


if __name__ == "__main__":
    # mat = [[int(input("give a number")) for i in range(C)] for j in range(R)]
    # print(mat)
    cost = [[1, 5, 3],
            [4, 8, 2],
            [6, 9, 31]]
    print(minCost(cost, 2, 2))
