# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        #initialize the left and right pointer
        #use Binary Search but no need to sort!
        l, r = 0 , n-1
        while l<=r:
            mid = l + ((r-l)//2)
            if mid > 0 and arr[mid] < arr[mid-1]:
                r = mid-1
            elif mid < n-1 and arr[mid] < arr[mid+1]:
                l = mid+1 
            else:
                return mid
