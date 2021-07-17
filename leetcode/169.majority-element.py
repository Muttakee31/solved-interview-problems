from collections import Counter

# class Solution(object):
def majorityElement(nums):
    """
    https://leetcode.com/problems/majority-element/
    """
    return Counter(nums).most_common(1)[0][0]