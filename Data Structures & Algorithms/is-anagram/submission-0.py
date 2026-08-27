class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS , countT = {}, {}

        # for dictionaries -> {letter, occurence}
        #first address obvious case
        if len(s) != len(t):
            return False
        for i in range(len(s)): #create hashMap for each string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #now we wanna loop through one of the hashmaps and see if it matches the contents of countT
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
                
        return True
