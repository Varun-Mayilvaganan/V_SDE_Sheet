class Solution:
	def twoSum(self, arr, target):
		# code here
		visited = set()
		
		for val in arr:
		    complement = target - val
		    if complement in visited:
		        return True
		    visited.add(val)
		    
		return False
