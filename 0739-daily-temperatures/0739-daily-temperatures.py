class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        mono_stack = []

        for i, num in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < num:
                stackInd = mono_stack.pop()[1]
                ans[stackInd] = i - stackInd
            mono_stack.append([num,i])
        
        return ans