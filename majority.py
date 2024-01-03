# n/3 times majority
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        count = n // 3
        counter = Counter(nums)
        result = []

        for num, freq in counter.items():
            if freq > count:
                result.append(num)

        return result