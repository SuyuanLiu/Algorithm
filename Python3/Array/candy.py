'''
Solution:
- Greedy
- 初始化一个candy数组，初始值为1
- 从左到右遍历，如果当前rating大于前面的，candy的值就在前一个基础上加1；
- 从右到左遍历，如果当前rating大于后面，并且candy值不大于后面的，candy就在后面基础上加1；
- 最后返回candy的和即可。
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
        
        candy = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
                
        return sum(candy)
