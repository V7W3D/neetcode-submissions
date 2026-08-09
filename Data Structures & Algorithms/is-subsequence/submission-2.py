class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
    
        i = 0
        j = 0

        while i < len(s):
            while j < len(t) and s[i] != t[j]:
                j+=1
            if j < len(t):
                i+=1
                j+=1
            else:
                return False
        
        return True
