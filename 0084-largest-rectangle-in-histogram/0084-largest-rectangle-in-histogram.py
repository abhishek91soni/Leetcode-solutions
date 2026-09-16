class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        pse = [-1] * n
        nse = [n] * n
        stack = []
        # Previous Smaller
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
            
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area