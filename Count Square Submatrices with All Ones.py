class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        # DP table same size as matrix
        dp = [[0] * n for _ in range(m)]
        
        total = 0  # this will store the result
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # First row or first column
                        dp[i][j] = 1
                    else:
                        # Recurrence relation
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    
                    total += dp[i][j]  # Add number of squares ending at (i,j)
        
        return total
