class Solution(object):
    """
    https://leetcode.com/problems/rotate-list/
    find the tail. connect head with tail.
    find the new tail of new list. Set its next to None. Return its previous element.
    """
    def rotateRight(self, head, k):
        if head is None:
            return None
        length = 0
        tail = head
        while(tail.next):
            length += 1
            tail = tail.next
        length += 1
        if k % length == 0:
            return head
        else:
            k = length - k % length
            
        leftOfNewHead = head
        while(k>1):
            leftOfNewHead = leftOfNewHead.next
            k -= 1
        newHead = leftOfNewHead.next
        leftOfNewHead.next = None
        tail.next = head
        
        return newHead