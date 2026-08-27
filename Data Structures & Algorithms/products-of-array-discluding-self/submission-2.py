class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Solution O(n2): two pointer and two loops. Go through every element in array and track product, skipping the num
        # prodArr = [0] * len(nums)

        # for i, num in enumerate(nums):
        #     prod = 1
        #     for j, num in enumerate(nums):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     prodArr[i] = prod  
        # return prodArr
        
        
        # Solution O(n)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        currNum = 1
        for i, num in enumerate(nums):
            prefix[i] = currNum
            currNum *= num
        
        currNum = 1 
        for i in range(len(nums) -1, -1, -1):
            postfix[i] = currNum
            currNum *= nums[i]

        # get prod pre * post to get prod of array
        return [pre * post for pre, post in zip(prefix, postfix)]

