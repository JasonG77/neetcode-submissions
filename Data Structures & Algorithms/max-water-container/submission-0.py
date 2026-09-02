class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE
        result = 0 #area

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                result = max(result, area) # return the max area by comparing it to the current result
        return result