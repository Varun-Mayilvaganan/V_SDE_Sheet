# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        left = 0
        total = sum(A)
        if N == 1:
            return 1
        for i in range(0,N):
            total -= A[i]
            if left == total:
                return i+1
            left += A[i]
        return -1    
            
