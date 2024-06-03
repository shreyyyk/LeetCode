class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checker(x,y,val,numx,numy):
            su=[]
            for j in range(y,numy):
                s=[]
                for i in range(x,numx):
                    if val==1:
                        if board[i][j]!='.' and board[i][j] in s:
                            return False
                        else:
                            s.append(board[i][j])
                    if val==2:
                        if board[j][i]!='.' and board[j][i] in s:
                            return False
                        else:
                            s.append(board[j][i])
                    if val==3:
                        if board[i][j]!='.' and board[i][j] in su:
                            return False
                        else:
                            su.append(board[i][j])
            return True
        
        return checker(0,0,1,9,9) and checker(0,0,2,9,9) and checker(0,0,3,3,3) and checker(3,0,3,6,3) and checker(6,0,3,9,3) and checker(0,3,3,3,6) and checker(3,3,3,6,6) and checker(6,3,3,9,6) and checker(0,6,3,3,9) and checker(3,6,3,6,9) and checker(6,6,3,9,9)
        