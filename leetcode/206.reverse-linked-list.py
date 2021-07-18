class Solution(object):
    def reverseList(self, head):
        """
        https://leetcode.com/problems/reverse-linked-list/
        approach was okay. just missed the pointer progression part in last line.
        """
        curr = head
        prev = None
        while(curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev