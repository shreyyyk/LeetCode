class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        count=Counter(arr)
        for elem in arr:
            if count[elem] == 1:
                k-=1
                if k==0:
                    return elem
        return ""
        