def displayList(head):
    result = [] 
    curr = head
    while curr:
        result.append(curr.data) 
        curr = curr.next
    return result
