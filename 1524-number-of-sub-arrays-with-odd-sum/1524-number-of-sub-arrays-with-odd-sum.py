class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)
        count = 0

        for start_index in range(n):
            current_sum = 0
            for end_index in range(start_index, n):
                current_sum += arr[end_index]
                if current_sum % 2 != 0:
                    count += 1

        return int(count % MOD)