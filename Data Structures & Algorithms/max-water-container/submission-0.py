class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_p = 0
        r_p = len(heights) - 1

        max_water = 0
        while l_p < r_p:
            max_water = max(max_water, min(heights[l_p], heights[r_p]) * (r_p - l_p))
            if heights[l_p] > heights[r_p]:
                r_p -= 1
            else:
                l_p += 1

        

        return max_water

        