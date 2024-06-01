class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashy={}
        i=0
        #if len(nums)==1:
        #    return False
        flag=1
        for i in range(len(nums)):
            num=nums[i]
            if num  in hashy:
                if(abs(hashy[num]-i)<=k):
                    flag=0
                    return True
                else:
                    flag=1
            
            hashy[num]=i
            
        if flag==1:
           return False