class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        hashy={}
        n=len(questions)
        hashy[n]=0
        for i in range(n-1,-1,-1):
            points=0
            if i+questions[i][1]+1 < n:
                points=hashy[i + questions[i][1] + 1]
            hashy[i]=questions[i][0]+points
            hashy[i]= max(hashy[i],hashy[i+1])
        return hashy[0]
                
                