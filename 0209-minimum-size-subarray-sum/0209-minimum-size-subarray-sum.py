class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l=0
        minlen=999999
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum >= target:
                minlen=min(minlen,r-l+1)
                currsum-=nums[l]
                l+=1
            
            r+=1

        return minlen
            