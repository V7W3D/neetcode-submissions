class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', "i","o", "u"}

        result = []
        for i in range(len(queries)):
            result.append(0)
            q = queries[i]
            for j in range(q[0], q[1]+1):
                w = words[j]
                if w[0] in vowels and w[-1] in vowels:
                    result[i] += 1
        return result