class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        
        # Precompute palindrome table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    is_pal[i][j] = True
                elif j == i + 1:
                    is_pal[i][j] = (s[i] == s[j])
                else:
                    is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
        
        # Initialize dp array where dp[i] is the min cuts for first i characters (0 to i-1)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i - 1  # Maximum possible cuts (each character is a palindrome)
            if is_pal[0][i-1]:
                dp[i] = 0
                continue
            for j in range(1, i):
                if is_pal[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n]