class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        current = 0
        for nums in digits:
            current = current * 10 + nums
        current = current + 1
        result = []
        for nums in str(current):
            result.append(int(nums))
        return result
