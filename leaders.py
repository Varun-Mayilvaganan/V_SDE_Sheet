class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        res = []
        maX = -1
        for i in range(N-1,-1,-1):
            if A[i] >= maX:
                res.append(A[i])
                maX = A[i]
        return res[::-1]   
