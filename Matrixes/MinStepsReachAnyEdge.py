# Python3 program to find Minimum steps
# to reach any of the boundary
# edges of a matrix
from collections import deque

r = 4
c = 5


# Function to check validity
def check(i, j, n, m, mat):
    if 0 <= i < n and 0 <= j < m:
        if mat[i][j] == 0:
            return True

    return False


# Function to find out minimum steps
def findMinSteps(mat, n, m):
    indx = indy = -1

    # Find index of only 2 in matrix
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                indx = i
                indy = j
                break

        if indx != -1:
            break

    # Push elements in the queue
    q = deque()

    # Push the position 2 with moves as 0
    q.append([0, indx, indy])

    # If already at boundary edge
    if check(indx, indy, n, m, mat):
        return 0

    # Marks the visit
    vis = [[0 for i in range(r)] for i in range(r)]

    # Iterate in the queue
    while len(q) > 0:

        # Get the front of the queue
        it = q.popleft()

        # Pop the first element from the queue

        # Get the position
        x = it[1]
        y = it[2]

        # Moves
        val = it[0]

        # If a boundary edge
        if x == 0 or x == (n - 1) or y == 0 or y == (m - 1):
            return val

        # Marks the visited array
        vis[x][y] = 1

        # If a move is possible
        if check(x - 1, y, n, m, mat):

            # If not visited previously
            if not vis[x - 1][y]:
                q.append([val + 1, x - 1, y])

            # If a move is possible
        if check(x + 1, y, n, m, mat):

            # If not visited previously
            if not vis[x + 1][y]:
                q.append([val + 1, x + 1, y])

            # If a move is possible
        if check(x, y + 1, n, m, mat):

            # If not visited previously
            if not vis[x][y + 1]:
                q.append([val + 1, x, y + 1])

            # If a move is possible
        if check(x, y - 1, n, m, mat):

            # If not visited previously
            if not vis[x][y - 1]:
                q.append([val + 1, x, y - 1])

    return -1


# Driver Code
mat = [[1, 1, 1, 0, 1],
       [1, 0, 2, 0, 1],
       [0, 0, 1, 0, 1],
       [1, 0, 1, 1, 0]]

print(findMinSteps(mat, r, c))
