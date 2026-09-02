class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #key - number : value - index
        for idx, val in enumerate(nums):
            numTwo = target - nums[idx]
            if numTwo in seen:
                return [seen[numTwo], idx]
            seen[val] = idx