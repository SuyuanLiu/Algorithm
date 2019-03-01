# Binary Tree

Outline
- [Preminary](#背景知识)
- [DFS](#Binary-Tree-DFS-Traversal)
    - Preorder
    - Divide & Conquer
    - DFS template
    - Examples
- [BFS](#Binary-Tree-BFS-Traversal)
    - BFS template
- [Binary Search Tree](#Binary-Search-Tree)
    - validate, insert, delete
- [Summary](#Summary)



## 背景知识

1. 前中后序遍历  
- 前序：根 左 右
- 中序：左 根 右
- 后序：左 右 根

2. 平衡二叉树  
左右子树高度差不超过1.
优点：在这种树上做插入删除遍历，时间复杂度不会超过logn

3. 二叉搜索树（BST）   
左子树值 < 根节点值 < 右子树值  
根据不同定义，可能一边会有等号。

4. 红黑树

5. AVL树  
balanced BST



## Binary Tree DFS Traversal

### Preorder Traversal

前序遍历有三种方法：
- 非递归方法（推荐）
- 递归：遍历, traverse
- 递归：分治法, divide conquer

前序遍历还是不推荐用分治，但是要体会这个思想，90%二叉树的题目都用到了分治法；

traverse 并不是通用的，分治更通用；

### 分治法

用到分治法的典型是：merge sort，quick sort，二叉树。关于sort部分，详见[这里](./sort.md).

分治：分为两个步骤，divide（分），conquer（合）

遍历与分治的区别：遍历把result作为一个参数进行传递，而分治利用函数本身的返回值；从多线程角度去看，遍历没办法进行多线程操作，而分治可以，分治是把左右子树的结果分别保存到一个数组中，最后再把结果拼接起来，左右子树可以多线程同时去实现递归，不会影响最后的结果。

### DFS模板

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

### 例题

1. maximum depth of binary tree    TC:O(n)
2. balanced binary tree  
代码里面定义-1表示不平衡，在实际工程中应该尽量避免这种，最好是给函数返回两个value：depht, isBalanced.      TC:O(n)

3. binary tree maximum path sum

- sub problem：从根节点出发的最大路径
- 可以从任何节点出发，从任何节点结束，说明要至少包含一个节点；
- 有三种情况，max在左子树，max在柚子树，max跨过root
- maxpath至少包含一个点，singlepath可以不包含点
- 注意一般root为空，退出递归；


4. lowest common ancestor（一次查询）  
- 一种题型，是treenode有parent这个指针，就把当前的节点的parent的parent这样一直存下来，一直到root节点，这样存成一个list，另一个节点出发也存一个list，倒序遍历这两个list，第一个节点一定是相同的，都是root，找到最后相同的那个就是LCA。  
- 另一种，没有parent指针，用分治法。
分治法的函数返回值都有一个意义，这边这个函数返回的是在root下，node1和node2的公共祖先，如果root这个树里只包含一个点，那么就返回这个node；如果都不包含，就返回None；（leetcode高票答案超级赞👍）  
- 或者是，找从根节点出发到node1，node2的路径，存为两个list，找到这两个list最后一个相同的值；（这个稍微麻烦一点）



## Binary Tree DFS Traversal 

例子：binary tree level order traversal(层序遍历)
三种方法：
- 2 queue
- 1 queue + Dummy Node（在每一层后面加入比如#，这样就知道每一层在哪里结束，当pop到#时，不直接扔掉，把它放到队列的最后面）
- 1 queue（best）（利用queue的length）

BFS的题可以很明显看出来是BFS，比较简单，不难；
BFS没有递归的写法；（可以理解为递归就是DFS，DFS就是递归）

时空复杂度：关于二叉树的，就是分析每个点要操作几次，一共有几个点；
关于这题，每个点会被push进队列一次，从队列pop一次，是O(1)，一共n个点，一共是O(n)。
空间复杂度O（n）

## Binary Search Tree

1. validate binary search tree(验证是否为二叉查找树)
- 按照定义去判断，用分治法（要比较所有左子树是不是小于root，直接看左子树的最大值，返回值中要包括左子树的最大值）...(视频1.45.11秒)
- 看中序遍历，如果中序遍历是升序的，那么就是BST

2. search range in binary search tree
- 方法1:直接把所有的节点遍历一遍(O(n))
- 方法2:优化，分治法（1.47.34）
3. implement iterator of Binary Search Tree
- 本质：非递归中序遍历（1.52.56）
4. remove node in binary tree  
Solution 1:
- 找到这个点；找到左子树的最大值，用这个值去填补这个点（或者柚子树的最小值）
- 如果左子树没有最大值，直接把柚子树提上去即可；左子树的最大值被拿走，那边空掉了，再用那个点的左子树的最大值填上去  
Solution 2:
- leetcode答案！很不错！
- 分为三种情况，root==key，>, < 分别做不同的处理。



## Summary

递归：traverse ， divide and conquer
BFS template
非递归的前中后遍历（记住）
（非递归的前中后遍历，morris算法，就是在非递归的时候，用O(1)的额外空间，这个是利用了node的右指针，用完把它赋值为空，实际上改变了树的结构）

二叉树的时间复杂度基本都是O(n)





