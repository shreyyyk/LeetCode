class Solution:
    def isHappy(self, n: int) -> bool:
        squareHash={}
        sumHash={}
        for i in range(10):
            squareHash[i]=i*i
        
        while(n):
            s=0
            while(n>0):
                
                s=s+squareHash[n%10]
                n=n//10
            if s==1:
                return True
           
            if s in sumHash:
                return False
            else:
                sumHash[s]=0
            n=s           


        
            
        
        