class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while(numBottles>numExchange-1):
            ex=numBottles//numExchange
            rem=numBottles%numExchange
            ans+=ex
            numBottles=ex+rem
        return ans