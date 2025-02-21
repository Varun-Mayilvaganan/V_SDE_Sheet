# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            if (isBadVersion(mid+1) == True) and (isBadVersion(mid)== False):
                return mid+1
            elif (isBadVersion(mid+1) == True) and (isBadVersion(mid)== True):
                high = mid - 1
            else:
                low = mid + 1
        
            
                

                    


        
