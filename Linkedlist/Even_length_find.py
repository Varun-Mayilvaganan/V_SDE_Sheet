class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        if count % 2 == 0:
            return True
        return False
            
            
