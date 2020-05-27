"""
Search a Word in a 2D Grid of characters
Given a 2D grid of characters and a word, find all occurrences of given word in grid. A word can
be matched in all 8 directions at any point. Word is said be found in a direction if all characters
match in this direction (not in zig-zag form).

The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up and 4 Diagonal directions.
Example:
Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
word = "GEEKS"

Output: pattern found at 0, 0
pattern found at 0, 8
pattern found at 1, 0

Input:  grid[][] = { "GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
word = "EEE"

Output: pattern found at 0, 2
pattern found at 0, 10
pattern found at 2, 2
pattern found at 2, 12

The idea used here is simple, we check every cell. If cell has first character, then we one by one try all
 8 directions from that cell for a match. Implementation is interesting though. We use two arrays x[]
  and y[] to find next move in all 8 directions.
"""


class SearchInGrid:
    def __init__(self):
        self.R = None
        self.C = None
        self.directions = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]  # 8 dirs.

    # IN JAVA THIS CAN BE DONE LIKE THIS.
    # //Rows and columns in given grid
    #  static int R, C;
    # //searching in all 8 direction
    # static int[] x = { -1, -1, -1, 0, 0, 1, 1, 1 };
    # static int[] y = { -1, 0, 1, -1, 1, -1, 0, 1 };

    def patternSearch(self, grid, word):
        self.R = len(grid)
        self.C = len(grid[0])
        for row in range(self.R):
            for col in range(self.C):
                if self.search8Directions(grid, row, col, word):
                    print(word, " pattern found at (i,j)=" + str(row) + " " + str(col))

    def search8Directions(self, grid, row, col, word):
        if grid[row][col] != word[0]:
            return False

        for x, y in self.directions:
            rd, cd = row + x, col + y  # int k, rd = row + x[i], cd = col + y[i]; in java
            flag = True
            # First character is already checked, match remaining characters
            for k in range(1, len(word)):
                if 0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]:
                    # Moving in particular direction
                    rd += x
                    cd += y
                else:  # If out of bound or not matched, break
                    flag = False
                    break
            if flag:
                return True
        return False


if __name__ == '__main__':
    Grid = ["GEEKSFORGEEKS",
            "GEEKSQUIZGEEK",
            "IDEQAPRACTICE"]
    sig = SearchInGrid()

    sig.patternSearch(Grid, 'GEEKS')
    print('**********')
    sig.patternSearch(Grid, 'EEE')
    print('**********')
    sig.patternSearch(Grid, 'QSF')
