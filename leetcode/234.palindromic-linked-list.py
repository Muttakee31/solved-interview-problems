# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
                
    def isPalindrome(self, head: ListNode) -> bool:
        """
        https://leetcode.com/problems/palindrome-linked-list/
        could not solve. :(
        find the middle of the list and keep reversing it until then.
        Finally compare the reversed and original list from the middle point,
        """
        slow = fast = head
        prev = None
        while(fast and fast.next):
            fast = fast.next.next
            current, slow = slow, slow.next 
            current.next, prev = prev, current
        if fast:
            slow = slow.next
        
        while (slow is not None):
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
            
        return True