class Solution(object):
    def deleteNode(self, node):
        """
        https://leetcode.com/problems/delete-node-in-a-linked-list/
        just replace the next node data with current node.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next