class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        oneBack, twoBack = 2,1
        for i in range(3,n+1):
            current = oneBack + twoBack
            twoBack=oneBack
            oneBack=current
        return oneBack