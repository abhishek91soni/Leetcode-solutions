class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        next_greater = {}
        for num in reversed(nums2):
            while st and st[-1] <= num :
                st.pop()
            if st:
                next_greater[num] = st[-1]
            else:
                next_greater[num] = -1
            st.append(num)
        return [next_greater[num] for num in nums1]
        