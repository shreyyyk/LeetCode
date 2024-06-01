class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash={}
        yHash={}
        if len(t)!=len(s):
            return False
        for letter in s:
            if letter in sHash:
                sHash[letter]+=1
            else:
                sHash[letter]=1
        for letter in t:
            if letter not in sHash or sHash[letter]==0:
                return False
            sHash[letter]-=1
            
        return True