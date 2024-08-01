class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for detail in details:
            age_str=detail[11:13]
            