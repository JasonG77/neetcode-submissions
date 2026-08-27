class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = int1 + int 2
        #target - int1 = difference
        hashMap = {} #stores visited numbers
        for i, v in enumerate(nums):
            difference = target - v
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[v] = i
        return
