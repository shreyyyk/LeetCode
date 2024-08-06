class Solution:
    def minimumPushes(self, word: str) -> int:
        '''hashy={}
        for i in range(len(word)):
            if word[i] in hashy:
                hashy[word[i]]+=1
            else:
                hashy[word[i]]=1
        print(hashy)'''
        from collections import Counter
        hashy=Counter(word)
        if len(hashy.keys())<=8:
            return sum(hashy.values())
        else:
            lst=sorted(hashy.values(), reverse=True)
            count=0
            mul=1
            maxx=8
            while lst:
                curr=lst[:8]
                count+=(sum(curr)*mul)
                lst=lst[8:]
                mul+=1
        return count
            