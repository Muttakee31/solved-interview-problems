class Solution(object):
    def hasCycle(self, head):
        """
        https://leetcode.com/problems/linked-list-cycle/
        used floyd cycle detection algorithm
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while(slow is not None and fast is not None and fast.next is not None):
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False