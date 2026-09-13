class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            minimum = nums[i]
            maximum = nums[i]
            for j in range(i,n):
                minimum = min(nums[j], minimum)
                maximum = max(nums[j], maximum)
                total += maximum - minimum
        return total



