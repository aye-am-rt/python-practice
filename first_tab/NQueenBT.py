""" Backtracking Algorithm
The idea is to place queens one by one in different columns, starting from the leftmost column. When we 
place a queen in a column, we check for clashes with already placed queens. In the current column, 
if we find a row for which there is no clash, we mark this row and column as part of the solution.
If we do not find such a row due to clashes then we backtrack and return false.

1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column. 
   Do following for every tried row.
    a) If the queen can be placed safely in this row 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to
       a solution then return true.
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.
3) If all rows have been tried and nothing worked,
   return false to trigger backtracking."""


def TryNQueenSolutions(brd, cols, N):
    if cols >= N:
        return True
    for i in range(N):
        pass

    pass


def printSolution(brd):
    pass


def solveNQ(N):
    board1 = [[0 for i in range(N)] for j in range(N)]

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if not TryNQueenSolutions(board, 0, N):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True


if __name__ == "__main__":
    N = int(input("give size of square chess board- an Integer = ").strip())
    print(solveNQ(N))
