from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        # prefix[i] = number of valid words among words[0:i]
        prefix = [0]

        for word in words:
            is_vowel_string = word[0] in vowels and word[-1] in vowels
            prefix.append(prefix[-1] + int(is_vowel_string))

        result = []

        for left, right in queries:
            # The +1 is because prefix is one element longer than words
            result.append(prefix[right + 1] - prefix[left])

        return result