# right, down, left, up
# thats the pattern, use the walls for boundaries
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        ans = []

        top = 0
        bottom = ROWS - 1
        left = 0
        right = COLS - 1

        while top <= bottom and left <= right:

            # move from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # move from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # move from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # move from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
        
