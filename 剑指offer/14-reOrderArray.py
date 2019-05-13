'''
解题思路：
牛客题目要求不能改变偶数与偶数之间、奇数与奇数之间的相对位置关系，所以不能使用双指针的思路来做。

Solution 1
这题使用类似插入的做法，i最外层遍历，j从i往后遍历，找到第一个奇数，然后把这个奇数插入到i的位置。
这边在j循环中，当进行过一次奇数交换后就break了，这个思路其实可以写成
- 时间复杂度 O(n^2)
- 空间复杂度 O(1)

Solution 2
类似冒泡排序的思路，i控制外层循环，j从后往前走，当相邻的两个元素满足偶前奇后时就交换；
这边要注意j不能从i开始往后走，如果数组最开始几个是偶数连在一起的话，就没办法把第一个偶数移到后面去了。
- 时间复杂度 O(n^2)
- 空间复杂度 O(1)

Solution 3
使用两个额外的数组，分别放奇数和偶数。(这个比较简单就没去实现)
- 时间复杂度 O(n)
- 空间复杂度 O(n)


Test Cases：
- 全部都是奇数，全部都是偶数
- 前面一串偶数，后面奇数
- 空数组

'''
# -*- coding:utf-8 -*-
# Solution 1
class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j] % 2 == 1:
                    for k in range(j, i, -1):
                        array[k], array[k-1] = array[k-1], array[k]
                    break
        return array

# Solution 2
class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        for i in range(len(array)):
            for j in range(len(array)-1, i, -1):
                if array[j] & 0x1 == 1 and array[j-1] & 0x1 == 0:
                    array[j], array[j-1] = array[j-1], array[j]
        return array
