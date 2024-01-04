class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        exist_even = False
        for elem in nums:
            if elem % 2 == 0:
                if exist_even:
                    return True
                exist_even = True
        return False