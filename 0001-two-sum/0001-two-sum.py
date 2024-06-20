class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy={}
        for i,num in enumerate(nums):
            rem=target-num
            if rem in hashy:
                return [hashy[rem],i]
            hashy[num]=i
                