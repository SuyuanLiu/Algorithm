'''
解题思路：
Solution 1:
使用字典：遍历一遍数组，把每个数字出现的次数存放在字典中；然后遍历字典键值，判断是否有超过一半的数字。
时间复杂度 O(n)，空间复杂度 O(n)

Solution 2:
利用符合条件的数字出现次数大于其余数字之和。
设置两个遍历cnt, num。
符合条件的数字，即出现次数超过数组长度一半，那么该数字出现的次数大于其余数字出现次数之和。
遍历一遍数组，将当前遍历到的数字设置为符合条件的数字num
- 继续遍历，如果下一个数字与当前数字相同，cnt加1，不同则减1.
- 如果cnt为0，继续遍历，把下一个数字设置为符合条件的数字
- 最后剩下的数字就可能是最终结果，但要使用helper函数额外判断是否符合条件，因为有可能数组中不存在符合条件的数字
（如果符合条件的数字一定存在，最后剩下的那个数字一定是最终结果）
时间复杂度 O(n)，空间复杂度 O(1)

Test Cases：
- 空数组
- 存在符合条件的数字
- 不存在符合条件的数字

'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        # write code here
        if not nums:
            return 0
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for key in dic.keys():
            if dic[key] > len(nums) // 2:
                return key
        return 0

# Solution 2
class Solution:
    def helper(self, nums, num):
        cnt = 0
        for n in nums:
            if num == n:
                cnt += 1
        return cnt > len(nums) // 2
    
    def MoreThanHalfNum_Solution(self, nums):
        # write code here
        if not nums:
            return 0
        cnt, num = 0, 0
        for n in nums:
            if cnt == 0:
                num = n 
                cnt = 1
            elif n == num:
                cnt += 1
            else:
                cnt -= 1
        if cnt != 0 and self.helper(nums, num):
            return num
        return 0
