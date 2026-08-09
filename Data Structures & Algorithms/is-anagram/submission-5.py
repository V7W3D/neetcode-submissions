class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in sdict:
                return False
            else:
                if sdict[t[i]] < 1:
                    return False
                sdict[t[i]] -= 1
        
        return True