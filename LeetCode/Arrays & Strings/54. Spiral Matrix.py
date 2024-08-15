# https://leetcode.com/problems/spiral-matrix/description/
# Difficulty: Medium

# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix[0])
        n = len(matrix)

        res = []

        i, j = 0, 0


        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        dir = RIGHT

        UP_WALL = 0
        RIGHT_WALL = m
        DOWN_WALL = n
        LEFT_WALL = -1

        while len(res) != m * n:
            if dir == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i = i + 1
                j = j - 1
                RIGHT_WALL -= 1
                dir = DOWN
            
            elif dir == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i = i - 1
                j = j - 1
                DOWN_WALL -= 1
                dir = LEFT 

            elif dir == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i = i - 1
                j = j + 1
                LEFT_WALL += 1
                dir = UP

            elif dir == UP:
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                i = i + 1
                j = j + 1
                UP_WALL += 1
                dir = RIGHT


        return res
    

test = Solution()
print(test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))