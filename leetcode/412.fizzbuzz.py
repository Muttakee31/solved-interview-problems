class Solution(object):
    def fizzBuzz(self, n):
        """
        https://leetcode.com/problems/fizz-buzz/
        
        """
        ans = ['' for i in range(n)]
        for i in range(n):
            if (i+1) % 15 == 0:
                ans[i] = "FizzBuzz"
            elif (i+1) % 5 == 0:
                ans[i] = "Buzz"
            elif (i+1) % 3 == 0:
                ans[i] = "Fizz"
            else:
                ans[i] = str(i+1)
        
        return ans