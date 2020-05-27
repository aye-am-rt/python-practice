"""Check if a word exists in a grid or not
Given a 2D grid of characters and a word, the task is to check if that word exists in the grid or not.
 A word can be matched in 4 directions at any point.

The 4 directions are, Horizontally Left and Right, Vertically Up and Down.
Examples:

Input:  grid[][] = {"axmy",
                    "bgdf",
                    "xeet",
                    "raks"};   word = "geeks"
Output: Yes

a x m y
b g d f
x e e t
r a k s

Input: grid[][] = {"axmy",
                   "brdf",
                   "xeet",
                   "rass"};
Output : No
Source: Microsoft Interview

Approach: The idea used here is described in the steps below:

Check every cell, if the cell has first character, then recur one by one and try all 4 directions from
that cell for a match.
Mark the position in the grid as visited and recur in the 4 possible directions.
After recurring, again mark the position as unvisited.
Once all the letters in the word is matched, return true."""


def FindInAllDirections(grid, word, i, j, rows, cols, level):
    ln = len(word)
    if level == 1:
        return True
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return False

    if grid[i][j] == word[level]:
        temp = grid[i][j]  # Marking this cell as visited
        grid[i].replace(grid[i][j], "#")

        # finding subpattern in 4 directions
        res = (FindInAllDirections(grid, word, i - 1, j, rows, cols, level + 1) |
               FindInAllDirections(grid, word, i+1, j, rows, cols, level + 1) |
               FindInAllDirections(grid, word, i, j-1, rows, cols, level + 1) |
               FindInAllDirections(grid, word, i, j+1, rows, cols, level + 1))

        # marking this cell as unvisited again
        grid[i].replace(grid[i][j], temp)
        return res
    else:
        return False


def checkMatch(grid, word, rows, cols):
    ln = len(word)
    # if total characters in matrix is less then pattern length
    if rows * cols < 1:
        return False
    for i in range(rows):
        for j in range(cols):  # If first letter matches, then # recur and check
            if grid[i][j] == word[0]:
                if FindInAllDirections(grid, word, i, j, rows, cols, 0):
                    return True
    return False


if __name__ == "__main__":

    Grid = ["axmy",
            "bgdf",
            "xeet",
            "raks"]
    r, c = 4, 4
    # Function to check if word exists or not  
    if checkMatch(Grid, "geeks", r, c):
        print("Yes")
    else:
        print("No")
