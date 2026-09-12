class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixMax = [0]*n
        suffixMax = [0]*n
        Max = 0
        for i in range(n):
            Max = max(Max,height[i])
            prefixMax[i] = Max
        print(prefixMax)
        Max = 0
        for i in range(n-1, -1, -1):
            Max = max(Max, height[i])
            suffixMax[i] = Max
        print(suffixMax)
        total = 0
        for i in range(n):
            total += min(prefixMax[i], suffixMax[i]) - height[i]
        return total
