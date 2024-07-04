class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n == 0 :
            return 0
        if n == 1:
            return cost[0]
        hashy={}
        hashy[n]=0
        hashy[n-1]=cost[n-1]
        for i in range(n-2,-1,-1):
            hashy[i]=cost[i]+min(hashy[i+1],hashy[i+2])
        return min(hashy[0],hashy[1])
            