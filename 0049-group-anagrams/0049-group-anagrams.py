class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wHash={}
        for word in strs:
            sWord=''.join(sorted(word))
            if sWord in wHash:
                wHash[sWord].append(word)
            else:
                wHash[sWord]=[word]
            
            
        res=[]
        for key,values in wHash.items():
            res.append(values)
        return res