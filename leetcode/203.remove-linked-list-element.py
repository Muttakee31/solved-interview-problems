from classes.ListNode import ListNode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        https://leetcode.com/problems/remove-linked-list-elements/
        had to delete the head elements differently
        """
        if head is None:
            return None
    
        while(head is not None and head.val == val):
            head = head.next
        temp = head
        prev = None
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        
        return head
            