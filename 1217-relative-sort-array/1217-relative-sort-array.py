class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k=0
        hashy={}
        for elem in arr1:
            if elem in hashy:
                hashy[elem]+=1
            else:
                hashy[elem]=1
        res=[]
        rem_res=[]
        for elem in arr2:
            res.extend([elem]*hashy[elem])
            k+=hashy[elem]
        for elem in hashy:
            if elem not in arr2:
                rem_res.extend([elem]*hashy[elem])
        res.extend(sorted(rem_res))
        return res