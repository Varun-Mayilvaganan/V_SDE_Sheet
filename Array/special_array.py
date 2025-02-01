class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == nums[i + 1] % 2):  # Both even or both odd
                return False
        return True
