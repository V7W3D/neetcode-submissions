class Solution:

    def extract_alnum(self, s: str) -> str:
        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()
        return result



    def isPalindrome(self, s: str) -> bool:
        s_alnum = self.extract_alnum(s)
        s_len = len(s_alnum)
        
        for i in range(s_len//2):
            if s_alnum[i] != s_alnum[s_len - i -1]:
                return False
        
        return True

        

                
