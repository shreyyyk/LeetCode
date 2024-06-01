class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst=s.split()
        p2s={}
        s2p={}
        if len(lst)!=len(pattern):
            return False
        for i in range(len(lst)):
            c1=lst[i]
            c2=pattern[i]
            if(c1 in s2p and s2p[c1]!=c2)or(c2 in p2s and p2s[c2]!=c1):
                return False
            s2p[c1]=c2
            p2s[c2]=c1
        return True
