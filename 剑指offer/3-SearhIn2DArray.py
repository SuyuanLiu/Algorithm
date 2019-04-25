'''
解题思路：
二分思想。选取右上角（或者左下角）的数字 tmp，与它比较：
    if target == tmp，结束查找；
    if target > tmp，说明 target 在 tmp 的下面的行中；
    if target < tmp，说明 target 在 tmp 前面的列中；

时空复杂度：
- 时间复杂度 O(logmn)
- 空间复杂度 O(1)

Test Cases：
- 空数组
- 数组中没有target
- 数组中有target，target是最小值/最大值/普通值
'''

def searchIn2DArray(nums, target):
    if not nums:
        return False
    
    row, col = len(nums), len(nums[0])
    i, j = 0, col - 1
    while i < row and j >= 0:
        tmp = nums[i][j]
        if tmp > target:
            j -= 1
        elif tmp < target:
            i += 1
        else:
            return True
    return False
