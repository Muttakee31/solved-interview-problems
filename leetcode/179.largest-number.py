class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mycmp(a, b):
            if a + b < b + a:
                return 1
            elif a + b > b + a:
                return -1
            else:
                return 0
        
        nums = list(map(str, nums))
        nums.sort(key = functools.cmp_to_key(mycmp))
        
        s = ''.join(nums)
        
        return s