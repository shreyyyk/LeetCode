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
            if letter in ransomHash:
                ransomHash[letter]+=1
            else:
                ransomHash[letter]=1
        for key,values in ransomHash.items():
            if key in magHash:
                if magHash[key]-values<0:
                    return False
            else:
                return False
        return True