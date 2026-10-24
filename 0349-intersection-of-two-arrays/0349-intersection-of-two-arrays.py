class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersect = []
        for num in nums1:
            if num in nums2:
                if num in intersect:
                    continue
                intersect.append(num)
        return intersect