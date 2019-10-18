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


if __name__ == '__main__':
    for n in range(15,30):

        res = generateBalancedString(n)
        # print(res)

        res2 = generateBalancedString2(n)
        # print(res2)

        # print()
        print(res == res2)