class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=sorted(citations)
        #zc=0
        for i in range(len(n)):
            if len(n)-i<=n[i]:
                return len(n)-i
        return 0