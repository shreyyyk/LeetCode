class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        for c in words[0]:
            words[0]=words[0].replace(c,'',1)
            for i in range(1,len(words)):
                if c in words[i]:
                    flag=1
                    words[i]=words[i].replace(c,'',1)
                else:
                    flag=-1
                    break
            if flag==1:
                res.append(c)
        return res
        
            