class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumMax(nums) - self.sumMin(nums)

    def sumMin(self, nums):
        stack = []
        total = 0

        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or nums[stack[-1]] >= nums[i]):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                total += nums[j] * left * right
            stack.append(i)

        return total

    def sumMax(self, nums):
        stack = []
        total = 0

        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or nums[stack[-1]] <= nums[i]):
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                total += nums[j] * left * right
            stack.append(i)

        return total