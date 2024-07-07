class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos=0
        turn=1
        while time>0:
            if turn ==1:
                pos+=1
                
                if pos==n-1:
                    turn=-1
            else:
                turn =-1
                pos-=1
               
                if pos==0:
                    turn=1
            time-=1
        return pos+1