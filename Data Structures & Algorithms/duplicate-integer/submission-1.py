class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #by sorting them, you asssure that duplicates are next to each other
        nums.sort()
        for i in range(1, len(nums)):
            #nums[i-1] means you start from the last element in the list ONLY IF YOU START AT 0
            #In this case it means we are checking the element behind our current element at index i
            if(nums[i] == nums[i - 1]):
                return True
        return False
            
        