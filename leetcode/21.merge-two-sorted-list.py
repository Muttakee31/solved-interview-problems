from classes.ListNode import ListNode
class Solution(object):
    ListNode: ListNode

    def mergeTwoLists(self, l1, l2):
        """
        attempt to learn linked list in python. could not solve.
        """
        result = curr = ListNode(0)
        
        while(l1 or l2):
            if not l2:
                result.next = l1
                l1 = l1.next
            elif not l1:
                result.next = l2
                l2 = l2.next
            else:
                if l1.val <= l2.val:
                    result.next = l1
                    l1 = l1.next
                else:
                    result.next = l2
                    l2 = l2.next
            result = result.next
                
        return curr.next