class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Monotonic stack
        # res = [0] * len(temperatures)
        # stack = [] # [temp, idx]

        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackIdx = stack.pop()
        #         res[stackIdx] = i - stackIdx
        #     stack.append((t, i))

        # return res

        # DP
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res   