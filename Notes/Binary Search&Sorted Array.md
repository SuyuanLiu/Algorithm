# Binary Search

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


## 总结

- 分析题目，把题目转化为find first position of, find last position of的类型；
- while循环之后，一定要对start，end做判断，因为当数组只有一个数值的时候，就不会进入到while循环里面去；



## 题目练习

- [Binary Search](https://leetcode.com/problems/binary-search/)
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

