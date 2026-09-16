class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        ans = []
        for element in num:
            while stack and stack[-1] > element and k > 0:
                stack.pop()
                k -= 1
            stack.append(element)
        if k > 0:
            stack = stack[:-k]
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'
