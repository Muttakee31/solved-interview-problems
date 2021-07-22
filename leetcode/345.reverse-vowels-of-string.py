class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_pos = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                v_pos.append((i, s[i]))
        
        for i in range(len(v_pos)//2):
            s[v_pos[i][0]], s[v_pos[-i-1][0]] = v_pos[-i-1][1], v_pos[i][1]
        
        return "".join(s)