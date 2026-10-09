class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i+1) # add the remaining

            # decision NOT include nums[i]
            subset.pop()
            dfs(i+1) # add the remaining
            
        dfs(0)
        return res