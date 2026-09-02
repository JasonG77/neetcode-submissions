class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashOne = {}
        hashTwo = {}
        if len(s) != len(t): return False
        for c in s:
            if c in hashOne:
                hashOne[c] += 1
            else:
                hashOne[c] = 1
        for z in t:
            if z in hashTwo:
                hashTwo[z] += 1
            else:
                hashTwo[z] = 1
        return hashOne == hashTwo