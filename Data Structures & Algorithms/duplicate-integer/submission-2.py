class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize a hashset
       	#iterate through nums
       	#if its already found in out hashset - return true
        #add the integers to a hash tables as we loop
        #else -> false
        numbersSeen = set()
        for n in nums:
            if n in numbersSeen:
                return True
            numbersSeen.add(n)
        return False   