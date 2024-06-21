class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        initialSatisfy=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                initialSatisfy+=customers[i]
        maxMinuteSatisfy=0
        for i in range(minutes):
            if grumpy[i]==1:
                maxMinuteSatisfy+=customers[i]
        currMax=maxMinuteSatisfy
        for i in range(minutes,len(customers)):
            if grumpy[i-minutes]==1:
                maxMinuteSatisfy-=customers[i-minutes]
            if grumpy[i]==1:
                maxMinuteSatisfy+=customers[i]
            currMax=max(currMax,maxMinuteSatisfy)
        return initialSatisfy + currMax