class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        for index in range(length - 1, -1, -1):
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] - dp[index + X][max(max_till_now, X)],
                    )
        return dp[0][1]