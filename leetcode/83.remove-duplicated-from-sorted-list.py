from classes.ListNode import ListNode
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        """
        if head is None:
            return head
        temp = head
        while(temp.next):
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head