# 0th row and 0th col are all 1s because there's only one path to those cells

# iterate through everything else and take the sum of anything to the left and above = unique paths to that cell

# last cell in the grid is where answer is stored, ez pz

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1]*n for _ in range(m)]
        print(dp)

        for r in range(1, m):
            for c in range(1, n):
    
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        
        return dp[-1][-1]

       

    
