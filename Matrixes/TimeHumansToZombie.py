"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent
(up/down/left/right) human beings into zombies every hour. Find out how many hours does it take
 to infect all humans?
Example:
Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2
Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]"""


def minHour(rows, columns, grid):
    if not rows or not columns:
        return 0

    q = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j] == 1]
    print(q)  # this is two know where(co-ordinate) of zombies(1) are present in matrix.

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #            [go-down, go-up, go-right, go-left] add one of this to any cell i,j to go in req direction
    time = 0

    while True:
        new = []
        for [i, j] in q:
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni, nj])
        q = new
        if not q:
            break
        time += 1

    return time


if __name__ == '__main__':
    mat = [[0, 1, 1, 0, 1],
           [0, 1, 0, 1, 0],
           [0, 0, 0, 0, 1],
           [0, 1, 0, 0, 0]]
    rs = 4
    cols = 5
    print("total Min days to convert totally = ")
    print(minHour(rs, cols, mat))
