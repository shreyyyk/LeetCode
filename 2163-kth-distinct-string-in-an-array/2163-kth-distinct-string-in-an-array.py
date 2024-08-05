class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashy={}
        for elem in arr:
            if elem in hashy:
                hashy[elem]+=1
            else:
                hashy[elem]=1
        for key in hashy.keys():
            if hashy[key] == 1:
                k-=1
                if k==0:
                    return key
        return ""
        