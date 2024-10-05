class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        s2_dict = {}
        
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        
        for i in range(len(s2)):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
            
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                if s2_dict[left_char] == 1:
                    del s2_dict[left_char]
                else:
                    s2_dict[left_char] -= 1
            
            if s1_dict == s2_dict:
                return True
        
        return False
