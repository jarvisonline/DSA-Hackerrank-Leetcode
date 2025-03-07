class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(ch) for ch in s if ch.isdigit()}  
        if len(digits) < 2:
            return -1
        return sorted(digits, reverse=True)[1]  
