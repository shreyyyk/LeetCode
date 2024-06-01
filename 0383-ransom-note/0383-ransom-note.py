class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magHash={}
        ransomHash={}
        for letter in magazine:
            if letter in magHash:
                magHash[letter]+=1
            else:
                magHash[letter]=1
        for letter in ransomNote:
            if letter not in magazine:
                return False
            magHash[letter]-=1
            if magHash[letter]<0:
                return False
        return True