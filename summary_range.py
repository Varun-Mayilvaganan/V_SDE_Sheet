# 
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                result.append(str(start) if start == end else f"{start}->{end}")
                start = end = num

        result.append(str(start) if start == end else f"{start}->{end}")
        return result
