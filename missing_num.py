class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_len = len(nums)
        p = list(range(arr_len + 1)) 
        nums.sort()

        for i in range(arr_len):
            if nums[i] != p[i]:
                return p[i]


        return p[-1]