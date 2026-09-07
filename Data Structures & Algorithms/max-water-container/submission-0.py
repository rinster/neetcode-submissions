class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        largest_area = 0


        # while l < r
            # calc max area l * w of the smallest height
            # update largest area if largest
            # decrement smallest of l, r pointer
        
        while l < r:
            max_area = min(heights[l], heights[r]) * (r - l)
            largest_area = max(largest_area, max_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return largest_area

        