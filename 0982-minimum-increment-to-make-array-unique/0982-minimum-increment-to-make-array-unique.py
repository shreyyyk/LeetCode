class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        count=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                increment=nums[i-1]-nums[i]+1
                nums[i]+=increment
                count+=increment
        return count