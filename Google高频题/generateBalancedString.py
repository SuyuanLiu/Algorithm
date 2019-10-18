'''
@lsy, 2019.10.19

Problem: Balanced String
Balanced String只由'0', '1'构成，同时满足连续三个位置上的数字不相同。问：
给定长度n，一共有多少种balanced string。
给定长度n，生成所有的balanced string。

Solution：DFS
我自己写的代码，会额外使用空间。另一份代码是一亩三分地网友提供的代码，感觉更简洁一些。

代码验证：两个代码对比过实验结果，是一致的。

题目链接：
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=556706&extra=page%3D1%26filter%3Dtypeid%26typeid%3D1019&page=1
'''
# Recommended Solution
def generateBalancedString2(n):
    if n < 1:
        return 

    res = []
    def dfs(prepath):
        if len(prepath) >= 3 and (prepath[-3:] == '000' or prepath[-3:] == '111'):
            return 
        
        if len(prepath) == n:
            res.append(prepath)
            return 

        dfs(prepath + '0')
        dfs(prepath + '1')

    dfs('')
    return res


# My Solution
def generateBalancedString(n):
    if n == 0:
        return 
    if n == 1:
        return ['0', '1']
    else:
        return dfs(['0', '1'], n-1)

def dfs(path, n):
    res = []
    for s in path:
        if len(s) > 1 and s[-1] == s[-2]:
            res.append(s + str(int(s[-1]) ^ 1))
        else:
            res.append(s + '0')
            res.append(s + '1')
    
    if n == 1:
        return res
    else:
        return dfs(res, n-1)
    
