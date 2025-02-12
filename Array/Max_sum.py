class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calculate_sum(n):
            total = 0
            while n > 0:
                rem = n % 10
                total += rem
                n = n//10
            return total

        unique_sum = {}
        max_sum = -1
        for num in nums:
            each_sum = calculate_sum(num)
            # If this sum of digits is already in the dictionary, we check for the maximum sum
            if each_sum in unique_sum:
                max_sum = max(max_sum, num + unique_sum[each_sum])
            # Store or update the value for this sum of digits
            unique_sum[each_sum] = max(num, unique_sum.get(each_sum, -1))

        return max_sum



            


