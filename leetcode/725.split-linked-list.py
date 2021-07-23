class Solution(object):
    def splitListToParts(self, head, k):
        """
        https://leetcode.com/problems/split-linked-list-in-parts/
        calculate the length
        get the value of smallest split.
        iterate and save the split ends to a list.
        if reminder is greater than 1. add extra 1 member to front splits.
        if split count is larger than list length, add empty list.
        """
        li = list()
        nullGroup = list()
        l=0
        if head is None:
            for i in range(k):
                li.append(None)
            return li
        temp = head
        while(temp.next):
            temp = temp.next
            l+=1
        l+=1
        
        res = l // k
        rem = l % k
        while(head):
            li.append(head)
            for i in range(res):
                temp = head
                head = head.next
            if rem > 0:
                temp = head
                head = head.next
                rem -= 1
            nullGroup.append(temp)
        
        for n in nullGroup:
            n.next = None
        dif = k - l
        while (dif > 0):
            li.append(None)
            dif -= 1
        return li        
        