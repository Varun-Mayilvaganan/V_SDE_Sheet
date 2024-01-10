
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()
        
        if len(arr) >= 3:
            return arr[-3]
        else:
            return max(arr)
