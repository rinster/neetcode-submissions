class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # iterative
        # n = len(nums)
        # permutations = []
        # stack = [[]]

        # while stack:
        #     curr = stack.pop()

        #     if len(curr) == n:
        #         permutations.append(curr)
            
        #     for num in nums:
        #         if num not in curr:
        #             stack.append(curr + [num])
        # return permutations

    
        output = []

        def helper(perm):
            if len(perm) == len(nums):   # full-length arrangement found
                output.append(perm[:])   # copy, since perm keeps changing
                return
            for val in nums:
                if val not in perm:      # skip values already used (assumes unique nums)
                    perm.append(val)     # choose
                    helper(perm)         # explore
                    perm.pop()           # undo

        helper([])
        return output