# 二分法总结

时间复杂度要求是O(log(N)),一般就是二分查找；
所有题目解法都在：https://github.com/SuyuanLiu/Leetcode. 
代码里面有思路的详细解释。
## 二分法模板
使用以下模板，针对不同的问题改变判断条件即可；
''' python
def binarySearch(self, num, target):
    if not num:
        return -1
    start, end = 0, len(num) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == num[mid]:
            return start
        elif target > num[mid]:
            start = mid + 1
        else:
            end = mid -1
    return -1
'''

## 典型题目：
### 典型二分以及二分变形
1. [Binary Search](https://leetcode.com/problems/binary-search/) 
    标准的二分搜索，直接利用模板即可；
2. [Search Insert Position](https://leetcode.com/problems/search-insert-position/) 
    套用二分模板，注意边界条件的判断；
3. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
    - 这个题目是把一个有序数组在某一点旋转，然后再寻找目标值；
    - 关键在于：旋转后的数组，进行二分搜索，一定有至少有一半的数组是有序的，判断target是否在这段有序的数组里面即可；
4. [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
    - 与上一道题目类似，只是数组里面多了重复元素；
    - 多了一个对重复元素的处理，元素重复的话，直接把指针向下一个位置移动，以忽略重复元素的影响；

### 幂，开方，除法
1. [Pow(x,n)](https://leetcode.com/problems/powx-n/)
    - 把幂数n转化为二进制形式，拆成幂指数相加的模式，x^(a+b+c) = (x^a)(x^b)(x^c)
    - 依次计算x的1,2,4,8,16...次方，把对应二进制为1的位置对应相乘；
2. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
    - 在[0,x]之间二分搜索根；
3. [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)
    - 除法就是看被除数中有几个除数，转化为减法；
    - 每次进行减法，除数翻倍；

### 两个有序数组的中位数
[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
两种方法：归并排序(O(N)), 二分搜索(O(logN))
二分搜索：对长度较短的数组进行划分，那么另一个数组的分割线位置随之固定；来回移动短数组的分割线，使得所有分割线左侧数值小于右侧；
