class Solution:
    def modularNode(self, head, k):
        # Code Here
        curr = head
        # to return the indexes which is divisible by 'k'
        mod_node = -1
        idx = 1
        # traverse through the LL
        while curr:
            if idx % k == 0:
                mod_node = curr.data
            curr = curr.next
            idx += 1
        # returns -1 if not present
        return mod_node
