class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        l,r = 0, len(heights) - 1

        while l<r:
            min_h = min(heights[l], heights[r])
            width = r - l

            area = min_h * width

            max_a = max(max_a, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_a
