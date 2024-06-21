class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left=0
        ans=0
        right=minutes
        maxSum=0
        
        while right<=len(customers):
            currSum=0
            for i in range(left,right):
                if grumpy[i]==1:
                    currSum+=customers[i]
            maxSum=max(maxSum,currSum)
            left+=1
            right+=1
        for i in range(len(customers)):
            if grumpy[i]==0:
                ans+=customers[i]
        return ans+maxSum