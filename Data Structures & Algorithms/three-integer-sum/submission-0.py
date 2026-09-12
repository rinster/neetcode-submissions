class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break # < --- not return
            
            # Skip duplicates in first numbers
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # continue skipping duplicates
                    while l < r and nums[l] == nums[l -1]:
                        l += 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1

        return res