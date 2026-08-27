class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #{value : index}
        for index, val in enumerate(nums):
            wantedNum = target - nums[index]
            if wantedNum in seen:
                return [seen[wantedNum], index]
            seen[val] = index