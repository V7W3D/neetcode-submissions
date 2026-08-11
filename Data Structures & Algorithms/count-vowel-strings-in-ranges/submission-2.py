class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i','o', 'u'}

        result = []
        exclusions = set()
        for i in range(len(queries)):
            result.append(0)
            q = queries[i]
            indices = set(range(q[0], q[1]+1)) - exclusions
            for j in indices:
                w = words[j]
                if w[0] in vowels and w[-1] in vowels:
                    result[i] += 1
                else:
                    exclusions.add(w)
        return result