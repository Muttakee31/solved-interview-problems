class Solution(object):
    def oddEvenList(self, head):
        """
        https://leetcode.com/problems/odd-even-linked-list/
        set two heads.
        iterate to set next of every node to its next.
        connect the two list.
        """
        if head is None or head.next is None:
            return head
        temp = head
        second_head = head.next
        is_odd = False
        while(temp.next and temp.next.next):
            temp1 = temp
            temp = temp.next
            temp1.next = temp.next
            is_odd = not is_odd

        if is_odd:
            temp.next.next = second_head
            temp.next = None
        else:
            temp.next = second_head
        return head
        