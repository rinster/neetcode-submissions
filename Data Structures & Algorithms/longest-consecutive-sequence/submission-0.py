class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_longest = 0
        numSet = set(nums)
        #    x              
        # [2,20,4,10,3,4,5]

        # currLong 4
        # max long = 4

        # loop thru nums
        # if num in leftmost num
        # -> init curr len
        # # WHILE check for right num and incre curr len
        # set max_longest if currLen is longer


        for num in nums:
            if (num - 1) not in numSet:
                curr_longest = 1
                while (num + curr_longest) in numSet:
                    curr_longest += 1
                max_longest = max(curr_longest, max_longest)

        return max_longest
                
        