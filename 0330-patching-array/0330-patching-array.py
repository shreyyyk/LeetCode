class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing=1
        patchCount=0
        idx=0
        while missing <=n:
            if idx<len(nums) and nums[idx]<= missing:
                missing+=nums[idx]
                idx+=1
            else:
                patchCount+=1
                missing<<=1
        return patchCount