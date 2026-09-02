class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        post = [1] * len(nums)

        currNum = 1
        for i, num in enumerate(nums):
            prefix[i] = currNum
            currNum *= num

        currNum = 1
        for idx, num in reversed(list(enumerate(nums))):
            post[idx] = currNum
            currNum *= num

        return [prefix * post for prefix, post in zip(prefix, post)]