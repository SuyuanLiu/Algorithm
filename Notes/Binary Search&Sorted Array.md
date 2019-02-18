# Binary Search

- [Binary Search Template](#inary-Search-通用模版)
- [Rotated Array](#Rotated-Array)
- [Find Median in Two Sorted Array](#Find-Median-in-Two-Sorted-Array)
- [Reverse in 3 steps](#三步翻转法)
- [Summary](#总结)
- [Leetcode](#题目练习)

## Binary Search 通用模版

Question：在一个有序数组中，找到target的位置（第一个出现的位置，最后一个出现的位置，任意位置）。

Solution：二分法，比较target和数组中间的值，如果target小于数组中间的值，说明target在数组左侧；若大于则在数组的右侧；相等则找到了target。

下面给出二分法的模板（适用于二分法的各种场合），这边的代码是找到target出现的第一个位置。

``` python3
def binarySearch(nums, target):
  if not nums:
    return -1

  start, end = 0, len(nums) - 1

  while start + 1 < end:
    mid = start + (end - start) // 2
    if nums[mid] == target:
      end = mid
    elif nums[mid] > target:
      end = mid
    elif nums[mid] < target:
      start = mid

  if nums[start] == target:
    return start
  if nums[end] == target:
    return end

  return -1
```

代码解释：
- ``while start + 1 < end``这边退出while循环的情况是start，end相邻或者相交了。因为在有的二分法的题目中，不是要你找到那个位置，而是要找到这个之间的位置；
- 注意：如果用``while start < end``，当nums=[1,2]只有两个数时，开始时mid=1，某种条件下start=mid=1，这就变成死循环了；
- ``mid = start + (end - start) // 2``这是为了防止数据过大出现溢出（等价于：mid = (start + end) // 2)；
- ``if nums[mid] == target:   end = mid`` 这边是要找到第一个出现的位置，所以应该尽可能的往左边去找，所以让 end = mid；如果是要找最后一个出现的位置，那就要start = mid；
- 最后跳出while循环时，start和end相邻或相交，要再对start和end做判断；至于先判断start还是先判断end，看具体情况，这边是找第一个出现的位置，所以要先判断start，如果是要找最后一个出现的位置，那就要先判断end；

## Rotated Array

find minimum
find target
why O(n) with duplicates


## Find Median in Two Sorted Array（Hard）

find Kth element in two sorted array 姐妹题，find median就是找到第 (m+n)/2 大的数（如果两数组长度和为奇数的话）。


## 三步翻转法

假设有Rotate 数组，要求把它变为原来的样子（之前的有序数组），比如：4，5，1，2，3 --> 1,2,3,4,5

三步翻转法就是：（先找到翻转的点）
- 先翻转4，5，    变为 5，4，1，2，3
- 再翻转1，2，3， 变为 5，4，3，2，1
- 然后整体翻转，  变为 1，2，3，4，5


## 总结

- 分析题目，把题目转化为find first position of, find last position of的类型，使用二分法的模板；
- while循环之后，一定要对start，end做判断，因为当数组只有一个数值的时候，就不会进入到while循环里面去；
- rotated array要画图进行分析；
- Find Median in Two Sorted Array
- 三步翻转法

两个重难点：
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
  [Python3](Python3/BinarySearch/searchRotated.py)
- [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)   
  [Python3](Python3/BinarySearch/findMedianSortArrays.py)



## 题目练习

- [Binary Search](https://leetcode.com/problems/binary-search/)
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

Rotated Array
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Median of Two Sorted Array
- [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)


Array
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

三步翻转法
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

