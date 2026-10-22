class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = set(nums)
        if len(result) != len(nums):
            return True
        return False