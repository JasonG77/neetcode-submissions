class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Plan out the code
        #I would loop through
        sortedS = sorted(s)
        sortedT = sorted(t) 
        n = len(s)
        m = len(t)
        # loop through entire string
        # if every character is the same then return true
        # else return False
        d = ''.join(sortedS)
        c = ''.join(sortedT)
        if d == c:
            return True

        return False