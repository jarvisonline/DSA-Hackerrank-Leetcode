class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        s = str(abs(x))[::-1]
        result = int(s)
        if negative:
            result = -result
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
