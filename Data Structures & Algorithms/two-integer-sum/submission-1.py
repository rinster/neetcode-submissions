class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} # num : index
        for i, num in enumerate(nums):
            seen = target - num
            if seen in my_dict:
                return [my_dict[seen], i]
            else:
                my_dict[num] = i
                #save the curr num and index


        