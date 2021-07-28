class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
        """
        sum = 0
        for w in words:
            n = len(w)
            i = 0
            while i < n:
                if w.count(w[i]) > chars.count(w[i]):
                    break
                i += 1
            # print(i)
            if i == n:
                sum += n
        
        return sum