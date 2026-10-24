class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = nums[0]
        for i in range(1,len(nums)):
            nums[i] += running_sum
            running_sum = nums[i]
        return nums
