class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        first, last = -1, -1

        # Find first occurrence
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid  # Potential first occurrence
                high = mid - 1  # Search left for earlier occurrences
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # Reset low and high for last occurrence search
        low, high = 0, len(nums) - 1

        # Find last occurrence
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid  # Potential last occurrence
                low = mid + 1  # Search right for later occurrences
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]
