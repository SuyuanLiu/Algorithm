'''
@lsy 2019.11.22
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        res = [[1], [1,1]]
        if numRows < 3:
            return res[:numRows]
        
        for n in range(2, numRows):
            tmp = [1 for _ in range(n+1)]
            preNum = res[-1]
            for i in range(1, n):
                tmp[i] = preNum[i-1] + preNum[i]
            res.append(tmp)
            
        return res