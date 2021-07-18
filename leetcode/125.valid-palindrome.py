class Solution(object):
    def isPalindrome(self, s):
        """
        https://leetcode.com/problems/valid-palindrome/
        should have used alnum() function
        """
        x = ''
        for i in range(len(s)):
            if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >='0' and s[i]<='9'):
                x += s[i]
        
        for i in range(len(x)//2):
            if x[i].lower() != x[-i-1].lower():
                return False
        return True

        """
        alternate solution: uses O(1) space and O(N/2) time.
        def isPalindrome(self, s):
            l, r = 0, len(s)-1
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1
                while l <r and not s[r].isalnum():
                    r -= 1
                if s[l].lower() != s[r].lower():
                    return False
                l +=1; r -= 1
            return True
        """