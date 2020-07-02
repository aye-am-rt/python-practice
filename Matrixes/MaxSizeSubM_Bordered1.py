"""
Given a matrix of ‘O’ and ‘X’, find the largest sub-square surrounded by ‘X’
Given a matrix where every element is either ‘O’ or ‘X’, find the largest subsquare surrounded by ‘X’.
In the below article, it is assumed that the given matrix is also square matrix. The code given below can
be easily extended for rectangular matrices.

Examples:

Input: mat[N][N] = { {'X', 'O', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'O', 'X', 'O'},
                     {'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'O'},
                 };
Output: 3
The square submatrix starting at (1, 1) is the largest submatrix surrounded by 'X'

Input: mat[M][N] = { {'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'X', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                 };
Output: 4
The square submatrix starting at (0, 2) is the largest submatrix surrounded by 'X'


A Simple Solution is to consider every square submatrix and check whether is has all corner edges filled
with ‘X’. The time complexity of this solution is O(N4).

We can solve this problem in O(N3) time using extra space. The idea is to create two auxiliary arrays
hor[N][N] and ver[N][N]. The value stored in hor[i][j] is the number of horizontal continuous ‘X’ characters
till mat[i][j] in mat[][]. Similarly, the value stored in ver[i][j] is the number of vertical continuous ‘X’
characters till mat[i][j] in mat[][]. Following is an example.

mat[6][6] =  X  O  X  X  X  X
             X  O  X  X  O  X
             X  X  X  O  O  X
             O  X  X  X  X  X
             X  X  X  O  X  O
             O  O  X  O  O  O

hor[6][6] = 1  0  1  2  3  4
            1  0  1  2  0  1
            1  2  3  0  0  1
            0  1  2  3  4  5
            1  2  3  0  1  0
            0  0  1  0  0  0

ver[6][6] = 1  0  1  1  1  1
            2  0  2  2  0  2
            3  1  3  0  0  3
            0  2  4  1  1  4
            1  3  5  0  2  0
            0  0  6  0  0  0
Once we have filled values in hor[][] and ver[][], we start from the bottommost-rightmost corner of matrix
and move toward the leftmost-topmost in row by row manner. For every visited entry mat[i][j], we compare the
values of hor[i][j] and ver[i][j], and pick the smaller of two as we need a square. Let the smaller of two
be ‘small’. After picking smaller of two, we check if both ver[][] and hor[][] for left and up edges
respectively. If they have entries for the same, then we found a subsquare. Otherwise we
try for small-1."""


def findSubSquareBorderedX(mat, sz):
    maxAns = 0
    hor = [[0 for i in range(sz)] for j in range(sz)]
    ver = [[0 for i in range(sz)] for j in range(sz)]

    if mat[0][0] == 'X':
        hor[0][0] = 1
        ver[0][0] = 1
    for i in range(sz):
        for j in range(sz):
            if mat[i][j] == 'O':
                ver[i][j] = hor[i][j] = 0
            else:
                if j == 0:
                    ver[i][j], hor[i][j] = 1, 1
                else:
                    ver[i][j], hor[i][j] = ver[i - 1][j] + 1, hor[i][j - 1] + 1

    # Start from the rightmost-bottommost corner element and find the largest sub-square with the help of
    # hor[][] and ver[][]
    for i in range(sz - 1, 0, -1):
        for j in range(sz - 1, 0, -1):
            small = min(hor[i][j], ver[i][j])
            # At this point, we are sure that there is a right vertical line and bottom  horizontal line of
            # length at least 'small'. We found a bigger square if following conditions are met:
            # 1)If side of square is greater than Max.
            # 2)There is a left vertical line of length >= 'small'
            # 3)There is a top horizontal line of length >= 'small'
            while small > maxAns:
                if ver[i][j - small + 1] >= small and hor[i - small + 1][j] >= small:
                    maxAns = small
                small -= 1

    return maxAns


if __name__ == '__main__':
    mt = [['X', 'O', 'X', 'X', 'X', 'X'],
          ['X', 'O', 'X', 'X', 'O', 'X'],
          ['X', 'X', 'X', 'O', 'O', 'X'],
          ['O', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'O', 'X', 'O'],
          ['O', 'O', 'X', 'O', 'O', 'O']]
    size = len(mt)
    print(findSubSquareBorderedX(mt, size))
