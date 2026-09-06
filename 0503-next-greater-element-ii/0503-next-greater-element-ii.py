class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        next_greater = [-1]* n
        st = []
        for i in range(2 * n-1,-1,-1):
            num = nums[i%n]
            while st and st[-1] <= num:
                st.pop()
            if i < n and st:
                next_greater[i] = st[-1]
            st.append(num)
        return next_greater