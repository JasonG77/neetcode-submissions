class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int) # creates a dictionary that keeps count
        # inside the count dicitonary - each ch is a key 
        #value will be number of occurences += 1
        for char in s:
            count[char] += 1

        for char in t:
            count[char] -= 1
        
        for countSoFar in count.values(): #you are looping through the values in count so value()
            if countSoFar != 0:
                return False

        return True
        