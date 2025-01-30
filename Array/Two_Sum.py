class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach 

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        #optimal approach

        visited = {}
        for i in range(len(nums)):
            val = nums[i]
            comp = target - val

            if comp in visited:
                return [i, visited[comp]]
            
            visited[val] = i
        return -1
