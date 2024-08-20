# https://leetcode.com/problems/valid-sudoku/description/
# Difficulty: Medium

# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution(object):
    def isValidSudoku(self, board):

        # Validate rows:
        for row in range(9):
            mySet = set()
            for col in range(9):
                item = board[row][col]
                if item in mySet:
                    return False
                elif item != '.':
                    mySet.add(item)

        # Validate columns:
        for row in range(9):
            mySet = set()
            for col in range(9):
                item = board[row][col]
                if item in mySet:
                    return False
                elif item != '.':
                    mySet.add(item)

        # Validate boxes:
        starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            s = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)

        return True
        
        return mySet


test = Solution()
print(test.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))