class Solution:
    def reverseList(self, head):
        # Code here
        
        # initially set the value to the Null; because incase of reversing the first value needs to point the None i.e, prev
        prev = None
        # setting the head node to curr variable
        curr = head
        
        while curr: # until it reaches last
        
            next_node = curr.next # to save the next node
            # due to  new links, the data will not break
            curr.next = prev
            prev = curr # hereafter the curr value will be the previous becuase it moves +1 further
            curr = next_node
        
        return prev
