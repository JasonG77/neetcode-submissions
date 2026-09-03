class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search - implementing a O(logn) algorithms - divide and conquer
        #1. Calculuate the mid point with L and R pointers
        #2. check where mid point lands vs. target
        #3. Divide appropiately
        #4. repeat until we find target or until L and R poitners overlap

        l, r = 0, len(nums) - 1
        while l <= r:
            midpoint = (l + r) // 2 #gets the index of the middle
            if nums[midpoint] < target:
                l = (midpoint + 1)
            elif nums[midpoint] > target:
                r = (midpoint - 1)
            else: 
                return midpoint
        #didnt find the target - > l and R overlaped
        return -1 
        
        