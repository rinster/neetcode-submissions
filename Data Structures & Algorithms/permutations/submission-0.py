class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # iterative
        n = len(nums)
        permutations = []
        stack = [[]]

        while stack:
            curr = stack.pop()

            if len(curr) == n:
                permutations.append(curr)
            
            for num in nums:
                if num not in curr:
                    stack.append(curr + [num])
        return permutations