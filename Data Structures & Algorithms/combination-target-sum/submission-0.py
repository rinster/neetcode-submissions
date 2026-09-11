class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:  # happy exit case
                res.append(cur.copy()) # <- always append a copy
                return

            # base case, could find sums   
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            # handle include
            dfs(i, cur, total + nums[i])
            cur.pop()
            # handle exclude
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res