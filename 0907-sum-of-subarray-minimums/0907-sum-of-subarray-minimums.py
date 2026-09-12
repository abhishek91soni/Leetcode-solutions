class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        pse = self.PSE(arr)
        nse = self.NSE(arr)
        total = 0
        mod = 10**9 + 7
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            freq = left * right * 1
            val = (freq * arr[i]) % mod
            total = (total + val) % mod
        return total

    def NSE(self, arr):
        n = len(arr)
        stack = []
        ans = [0]*n
        for i in range(n-1, -1, -1):
            currElelment = arr[i]
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else n
            stack.append(i)
        return ans
    def PSE(self, arr):
        n = len(arr)
        stack = []
        ans = [0]*n
        for i in range(n):
            currElement = arr[i]
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
        return ans