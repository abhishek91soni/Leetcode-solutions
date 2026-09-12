class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = 0
        rmax = 0
        l = 0 
        r = n-1
        total = 0
        while l != r:
            if height[l] <= height[r]:
                if lmax < height[l]:
                    lmax = height[l]
                total += lmax - height[l]
                l = l+1
            if height[l] > height[r]:
                if rmax < height[r]:
                    rmax = height[r]
                total += rmax - height[r]
                r = r - 1
        return total



