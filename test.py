# -*- coding:utf-8 -*-
class Solution:
    def findIdx(self, sequence, start, end):
        for i in range(start, end):
            if sequence[i] > sequence[end]:
                return i 
        return -1
    
    def helper(self, sequence):
        if len(sequence) < 2:
            return  True
        idx = self.findIdx(sequence, 0, len(sequence)-1)
        if idx != -1 and min(sequence[idx:-1]) < sequence[-1]:
            return False
        left = self.helper(sequence[:idx])
        right = self.helper(sequence[idx:-1])
        return left and right
    
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if self.helper(sequence):
            print('Yes')
        else:
            print('No')
# -*- coding:utf-8 -*-
class Solution:
    def findIdx(self, sequence, start, end):
        for i in range(start, end):
            if sequence[i] > sequence[end]:
                return i 
        return -1
    
    
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) < 2:
            return  True
        idx = self.findIdx(sequence, 0, len(sequence)-1)
        if idx != -1 and min(sequence[idx:-1]) < sequence[-1]:
            return False
        left = self.VerifySquenceOfBST(sequence[:idx])
        right = self.VerifySquenceOfBST(sequence[idx:-1])
        return left and right

s = Solution()
# a = [4,8,6,12,16,14,10]
a = [4,6,7,5]
print(s.VerifySquenceOfBST(a))
