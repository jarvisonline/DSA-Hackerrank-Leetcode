class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            s1=sorted(s)
            s2=sorted(t)
            if(s1==s2):
                return True
            else:
                return False
        