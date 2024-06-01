class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        nums.sort()
        long=1
        i=0
        if len(nums)==0:
            return 0
        while(i<=len(nums)-1):
            if nums[i]-nums[i-1]==0:
                count+=0
            elif nums[i]-nums[i-1]==1:
               count+=1
               long=max(count,long)
            else:
                long=max(count,long)
                count=1
            i+=1
        return long
            

        