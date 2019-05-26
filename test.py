def goodInRow(R, C, K, matrix):
    res = []
    for i in range(R):
        tmp = []
        left = 0
        min_, max_ = matrix[i][0], matrix[i][0]
        for j in range(1, C):
            min_, max_ = min(min_, matrix[i][j]), max(max_, matrix[i][j])
            if max_ - min_ > K:
                if j-1 != left:
                    tmp.append([left, j-1])
                left = j 
                min_, max_ = matrix[i][j], matrix[i][j]
            elif j == C - 1 and j != left:
                tmp.append([left, j])
        res.append(tmp)
    return res 


def findMaxInConsecutiveArea(s, e, margin):
    res = 0
    for i in range(s, e+1):
        tmp = margin[i]
        for j in range(len(tmp)):
            l, r = tmp[j]
            res = max(res, r-l+1)
            for k in range(i, e+1):
                



def findGoodSquare(R, C, K, matirx):
    margin = goodInRow(R, C, K, matrix)
    res = R 
    for i in range(R):

            
            
def main():
    t = int(input())
    for i in range(1, t+1):
        [R, C, K] = [int(s) for s in input().split(' ')]
        matrix = []
        for i in range(R):
            matrix.append([int(s) for s in input().split(' ')])
        res = findGoodSquare(R, C, K, matirx)
        print('Case #{}: {} {}'.format(i, res))

if __name__ =='__main__':
    main()



# m = [[15,10,20,15],[10,4,5,20],[20,5,4,10],[20,10,20,10]]
# res = goodInRow(4,4,8,m)
# for i in range(len(res)):
#     print(len(res[i]))
#     print(res[i])
