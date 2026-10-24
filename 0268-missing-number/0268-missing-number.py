class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            total_sum += nums[i]
        expected_sum = int((n * (n+1)) / 2)
        missing_number = expected_sum - total_sum
        return missing_number