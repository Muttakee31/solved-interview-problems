class Solution(object):
    def myAtoi(self, s):
        """
        https://leetcode.com/problems/string-to-integer-atoi/
        """
        s = s.lstrip()
        sign = 1
        start = 0
        pos_max = 2**31-1
        neg_max = -2**31
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        ans = ''
        for i in range(start, len(s)):
            if not (s[i] >= '0' and s[i] <= '9'):
                break
            ans += s[i]
        
        atoi = 0
        mult = sign
        for i in range(len(ans)-1, -1, -1):
            atoi += int(ans[i]) * mult
            if atoi > pos_max:
                return pos_max
            if atoi<neg_max:
                return neg_max
            mult *= 10
        
        return atoi
