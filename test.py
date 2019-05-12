class Solution():
    def __init__(self):
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def printNum(self, num):
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        if i == len(num):
            return 
        print(num[i:])

    def helper(self, num, idx):
        if idx == len(num):
            self.printNum(num)
            return 
        for i in range(10):
            num = num[:idx] + self.nums[i] + num[idx+1:]
            self.helper(num, idx+1)
    

    def printNmax(self, n):
        if n <= 0:
            return 
        num = '0' * n
        self.helper(num, 0)
    
s = Solution()
s.printNmax(3)
