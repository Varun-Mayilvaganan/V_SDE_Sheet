class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use two pointer method to solve
        slow, fast = head, head
        # until it reaches null and if it's not then both pointers should meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False
