class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashy={0:-1}
        summ=0
        
        for i in range(len(nums)):
            summ+=nums[i]
            
            if summ%k == 0 and i>1:
                return True
            if summ%k in hashy:
                if i-hashy[summ%k]>1:
                    return True
            else:
                hashy[summ%k]=i
        return False