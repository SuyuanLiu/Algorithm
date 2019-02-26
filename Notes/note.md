# DFS

前序遍历
- 非递归方法（推荐）
- 递归：遍历, traverse
- 递归：分治法, divide conquer

    遍历与分治的区别：遍历把result作为一个参数进行传递，而分治利用函数本身的返回值；从多线程角度去看，遍历没办法进行多线程操作，而分治可以，分治是把左右子树的结果分别保存到一个数组中，最后再把结果拼接起来，左右子树可以多线程同时去实现递归，不会影响最后的结果。

    分治：分为两个步骤，divide（分），conquer（合）

    前序遍历还是不推荐用分治，但是要体会这个思想，90%二叉树的题目都用到了分治法；

    traverse 并不是通用的，分治更通用；

分治法
- merge sort
- quick sort
- 二叉树

Sort
merge sort：
- 从中间分开，左边递归归并，右边递归归并，使得左边有序，右边有序，然后利用额外空间合并这两个有序数  组，然后再把合并好的数组倒腾到原来的数组里去（耗费很多时间）
- 分治思想，局部有序，最后整体有序；

quick sort
- 做partition，从数组中随机挑选一个数，比它小的放前面，大的放后面；（一般挑选中间的值，挑第一个或者最后一个也可以，只是容易构造它的最后情况）
- 分治思想，先整体有序，然后局部有序

merge sort：O(nlogn)  O(n)  稳定
quick sort：O(nlogn)  O(1)  不稳定

排序中nlogn的堆排序不是分治法，但也利用了这个思想；
实际中快排用的多一点，因为不耗费额外空间，归并排序还要把合并好的新数组放到之前的数组里去，也很耗时间；

稳定性：对于key-value情况，或者排坐标(1,1),(1,2),(1,3)按照x排...

时间复杂度分析：
归并：每次合并两个有序数组耗费的时间是O(n)，然后一半一半的分最后是logn；
     树状结构，每一层合并数组的时间加起来都是O(n),（合并n/2的数组为O(n)...）
快排：是平均复杂度为nlogn
     最好的情况nlogn，平均情况nlogn，最坏的情况n^2；
     最坏：每次partition之后的x都是最小或者最大的数（每次partition时间O(n)），最后要做n次；
     平均是按照概率来算的；
     （在网上看的一个方法，快排之前先把数组打乱一下） 


maximum depth of binary tree    TC:O(n)
balanced binary tree(代码里面定义-1表示不平衡，在实际工程中应该尽量避免这种，最好是给函数返回两个value：depht, isBalanced.)       TC:O(n)

二叉树的时间复杂度基本都是O(n)

binary tree maximum path sum
- sub problem：从根节点出发的最大路径
- 可以从任何节点出发，从任何节点结束，说明要至少包含一个节点；
- 有三种情况，max在左子树，max在柚子树，max跨过root
- maxpath至少包含一个点，singlepath可以不包含点
- 注意一般root为空，退出递归；


lowest common ancestor
一次查询

一种题型，是treenode有parent这个指针，就把当前的节点的parent的parent这样一直存下来，一直到root节点，这样存成一个list，另一个节点出发也存一个list，倒序遍历这两个list，第一个节点一定是相同的，都是root，找到最后相同的那个就是LCA。

另一种，没有parent指针，用分治法。
分治法的函数返回值都有一个意义，这边这个函数返回的是在root下，node1和node2的公共祖先，如果root这个树里只包含一个点，那么就返回这个node；如果都不包含，就返回None；（不是很理解）

我自己的想法是，找从根节点出发到node1，node2的路径，存为两个list，找到这两个list最后一个相同的值；


DFS模板：
``` python
# traversal
def traversal(root):
     if not root:
          return 

     traversal(root.left)
     traversal(root.right)

# divide and conquer
def dTraversal(root):
     if not root:
          return 

     # divide
     left = dTraversal(root.left)
     right = dTraversal(root.right)

     # conquer
     res = left + right... 
     return res
```


# BFS

binary tree level order traversal
(层序遍历)
三种方法：
- 2 queue
- 1 queue + Dummy Node（在每一层后面加入比如#，这样就知道每一层在哪里结束，当pop到#时，不直接扔掉，把它放到队列的最后面）
- 1 queue（best）（利用queue的length）

BFS的题可以很明显看出来是BFS，比较简单，不难；
BFS没有递归的写法；（可以理解为递归就是DFS，DFS就是递归）

时空复杂度：关于二叉树的，就是分析每个点要操作几次，一共有几个点；
关于这题，每个点会被push进队列一次，从队列pop一次，是O(1)，一共n个点，一共是O(n)。
空间复杂度O（n）


# 二叉查找树 BST

validate binary search tree(验证是否为二叉查找树)
直接看中序遍历，如果中序遍历是升序的，那么就是BST

两种方法：
- 按照定义去判断，用分治法（要比较所有左子树是不是小于root，直接看左子树的最大值，返回值中要包括左子树的最大值）...(视频1.45.11秒)
- 看中序遍历

题目：
在二叉树中插入节点
search range in binary search tree
     - 方法1:直接把所有的节点遍历一遍(O(n))
     - 方法2:优化，分治法（1.47.34）
implement iterator of Binary Search Tree
     - 本质：非递归中序遍历（1.52.56）
remove node in binary tree
     - (比较难)
     - 思路：  
          找到这个点
          找到左子树的最大值，用这个值去填补这个点（或者柚子树的最小值）

          如果左子树没有最大值，直接把柚子树提上去即可
          左子树的最大值被拿走，那边空掉了，再用那个点的左子树的最大值填上去



# Summary

递归：traverse ， divide and conquer
BFS template
非递归的前中后遍历（记住）
（非递归的前中后遍历，morris算法，就是在非递归的时候，用O(1)的额外空间，这个是利用了node的右指针，用完把它赋值为空，实际上改变了树的结构）

红黑树？（知道一下是什么）
AVL（balanced BST），不要花太多时间


# 概念类

前中后序遍历
平衡二叉树（优点：在这种树上做插入删除遍历，时间复杂度不会超过logn） 







    
