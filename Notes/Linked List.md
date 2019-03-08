# Linked List

Outline
- [Dummy Node](#Dummy-Node)
- [Basic Skills](#Basic-Skills)
- [Fast Slow Pointer](#Fast-Slow-Pointer)




## 题

- [remove duplicate from sorted list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)  32.12
- [reverse list]
- [reverse list II]  翻转m，n之间的，用到dummy node
- [merge two sorted list]
- [partition list]

Basic skills

insert a node 
remove a node
merge two list
reverse list
find middle of list(init: slow = head, fast = head.next)
sort list(nlogn): quick sort, or merge sort
reorder list



remove nth node from the end of list
linked list circle I, II

merge K sorted list(PriorityQueue，要用到一个数据结构就是堆，能找到最小值，add一个数，pop一个数，python应该不叫这个名字)
copy list with random pointer(对这个链表做deep copy) 1.31
    深度拷贝都可以用 hash 表，万能的工具， O（n）额外空间
    优化：不用额外空间，

关于hash表：
C++11: unordered map, map(实质是红黑树)
python: {}, dict()

convert sorted list to balanced binary search tree
(convert sorted arry to balanced bianry search tree)
如果list也用array的方法，要找middle，对于list花费时间是O（n），时间复杂度是nlogn
关键是找middle耗时间，可以在代码中用一个size，代替找array下标那种，时间复杂度就可以变为
   helper(head,size)  返回TreeNode, nextHead

## Dummy Node

if 语句特别多，考虑Dummy Node，会减少if 语句一般。

Dummy Node 的作用：当 Head 不确定时，使用 Dummy Node。


## Basic Skills


## Fast Slow Pointer

这种类型的题就那么两三道。