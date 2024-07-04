class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        hashy={}
        hashy[n]=0
        hashy[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            hashy[i]=nums[i]+(hashy[i+2] if i+2<n else 0)
            hashy[i]=max(hashy[i],hashy[i+1])
        return max(hashy[0],hashy[1])
