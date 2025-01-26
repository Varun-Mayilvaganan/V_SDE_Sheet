class Solution:
    def insertInMiddle(self, head, x):
        #code here
        new_node = Node(x)
        if head is None:
            return new_node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow  = slow.next
            fast = fast.next.next
        new_node.next = slow.next
        slow.next = new_node
        return head
