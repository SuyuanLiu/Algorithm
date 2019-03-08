# Leetcode

Leetcode solutions written by python3 and C++. 
- With short solution idea added in each solution. 
- A summary of each kind problem is concluded.
- Some questions can't find in leetcode, the questions details will be given at the top of the code.

If labels is :octocat: , it means it's a classical question.


## Index

- [Binary Search](#Binary-Search)
- [Two Pointer](#Two-Pointer)
- [Sort](#Sort)  
- [Binary Tree](#Binary-Tree)
- [Array](#Array)
- [String](#String)
- [Linked List](#Linked-List)
- [BFS](#BFS)
- [DFS](#DFS)
- [Dynamic Programming](#Dynamic-Programming)


## Binary Search

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Binary Search](https://leetcode.com/problems/binary-search/)| [C++](C++/BinarySearch/binarySearch.cpp), [Python3](Python3/BinarySearch/binarySearch.py)|标准二分|:octocat:|
|1|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)| [Python3](Python3/BinarySearch/intersection.py)|二分法**TODO**||
|2|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)| [Python3](Python3/BinarySearch/intersection2.py)|二分法**TODO**||
|3|[Pow(x,n)](https://leetcode.com/problems/powx-n/)| [Python3](Python3/BinarySearch/myPow.py)|二分思想|:octocat:|
|4|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)| [Python3](Python3/BinarySearch/countNodes.py)|二分思想|:octocat:|
|5|find nums[i]==i|[Python3](Python3/BinarySearch/search.py)|题目描述在代码内|:octocat:|
|6|[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)| [Python3](Python3/BinarySearch/searchInsert.py)|||
|7|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)| [Python3](Python3/BinarySearch/searchRotated.py)|||
|8|[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)| [Python3](Python3/BinarySearch/searchRotatedII.py)|||
|9|[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)| [Python3](Python3/BinarySearch/findMedianSortArrays.py)|二分+归并**TODO**|:octocat:|
|10|[Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)| [Python3](Python3/BinarySearch/divide.py)||:octocat:|
|11|[Sqrt(x)](https://leetcode.com/problems/sqrtx/)| [Python3](Python3/BinarySearch/mySqrt.py)||:octocat:|
|12|[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)| [Python3](Python3/BinarySearch/searchRange.py)|||
|13|[74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)| [Python3](Python3/BinarySearch/searchMatrix.py)|||
|14|[240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)| [Python3](Python3/BinarySearch/searchMatrixII.py)|Follow up added|:octocat:|
|15|[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)| [Python3](Python3/BinarySearch/firstBadVersion.py)|||
|16|[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)| [Python3](Python3/BinarySearch/findPeakElement.py)|||
|17|[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)| [Python3](Python3/BinarySearch/findMin.py)|||
|18|[154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)| [Python3](Python3/BinarySearch/findMinII.py)|||
|--|[Summary](Python3/BinarySearch/Summary-BinarySearch.md)|||   

[Back to Top](#index)



## Two Pointer

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| [C++](C++/TwoPointer/lengthOfLongestSubstring.cpp)||:octocat:|
|1|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)| [C++](C++/TwoPointer/maxArea.cpp)||:octocat:|
|2|[3Sum](https://leetcode.com/problems/3sum)| [C++](C++/TwoPointer/threeSum.cpp)||:octocat:|
|3|[3Sum Closest](https://leetcode.com/problems/3sum-closest/)| [C++](C++/TwoPointer/threeSumClosest.cpp)|||
|4|[4Sum](https://leetcode.com/problems/4sum/)| [C++](C++/TwoPointer/fourSum.cpp)|||
|5|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)| [C++](C++/TwoPointer/removeDuplicates.cpp)， [Python3](Python3/Array/removeDuplicates.py)|||
|6|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)| [C++](C++/TwoPointer/removeDuplicatesII.cpp), [Python3](Python3/Array/removeDuplicatesII.py)|||
|7|[Implement strStr()](https://leetcode.com/problems/implement-strstr/)| [C++](C++/TwoPointer/strStr.cpp)|||
|8|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)| [C++](C++/TwoPointer/trap.cpp)|Solution3不怎么理解|:octocat:|
|9|[Sort Colors](https://leetcode.com/problems/sort-colors/) | [C++](C++/TwoPointer/sortColors.cpp)||:octocat:|
|10|[Partition List](https://leetcode.com/problems/partition-list/)| [C++](C++/TwoPointer/partition.cpp)|O(n)O(1) TODO||
|11|[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)| [C++](C++/TwoPointer/merge.cpp), [Python3](Python3/Array/merge.py)|||
|12|[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)| [C++](C++/TwoPointer/isPalindrome.cpp)|||
|13|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/submissions/)| [C++](C++/TwoPointer/hasCycle.cpp)|||
|14|[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)| [C++](C++/TwoPointer/detectCycle.cpp)||:octocat:|
|15|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)| [C++](C++/TwoPointer/minWindow.cpp)||:octocat:|   

[Back to Top](#index)



## Sort

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Bubble Sort](https://www.lintcode.com/problem/sort-integers/description)| [C++](C++/Sort/Bubble.cpp)|冒泡|:octocat:|
|1|[Select Sort](https://www.lintcode.com/problem/sort-integers/description)| [C++](C++/Sort/Select.cpp)|选择|:octocat:|
|2|[Insert Sort](https://www.lintcode.com/problem/sort-integers/description)| [C++](C++/Sort/Insert.cpp)|插入|:octocat:|
|3|[Merge Sort](https://www.lintcode.com/problem/sort-integers/description)| [Python3](Python3/Sort/Merge.py), [C++](C++/Sort/Merge.cpp)|归并|:octocat:|
|4|[Quick Sort](https://www.lintcode.com/problem/sort-integers/description)| [C++](C++/Sort/Quick.cpp)|快排|:octocat:|
|5|[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)| [Python3](Python3/Sort/findKthLargest.py)||:octocat:|
|--|[Summary](https://suyuanliu.github.io/2018/09/20/Alg-Sort/)|||

[Back to Top](#index)



## Binary Tree

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Same Tree](https://leetcode.com/problems/same-tree/submissions/)| [C++](C++/BinaryTree/isSameTree.cpp)|||
|1|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[Python3](Python3/BinaryTree/maxDepth.py), [C++](C++/BinaryTree/maxDepth.cpp)||:octocat:|
|2|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)| [Python3](Python3/BinaryTree/inorderTraversal.py), [C++](C++/BinaryTree/inorderTraversal.cpp)|中序遍历|:octocat:|
|3|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)| [Python3](Python3/BinaryTree/preorderTraversal.py), [C++](C++/BinaryTree/preorderTraversal.cpp)|前序遍历|:octocat:|
|4|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)| [Python3](Python3/BinaryTree/postorderTraversal.py), [C++](C++/BinaryTree/postorderTraversal.cpp)|后序遍历|:octocat:|
|5|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| [Python3](Python3/BinaryTree/levelOrder.py)|层序遍历|:octocat:百度|
|6|[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)| [Python3](Python3/BinaryTree/zigzagLevelOrder.py)|z字形遍历|:octocat:|
|7|[Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)| [Python3](Python3/BinaryTree/buildTree.py)|重构二叉树,TODO:非递归|:octocat:|
|8|[Construct Binary Tree from Inorder and Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)| [Python3](Python3/BinaryTree/buildTree2.py)|TODO:非递归||
|9|[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)| [Python3](Python3/BinaryTree/isSymmetric.py)||:octocat:|
|10|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)| [Python3](Python3/BinaryTree/invertTree.py)||:octocat:|
|11|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)| [Python3](Python3/BinaryTree/isBalanced.py)||:octocat:|
|12|[Path Sum](https://leetcode.com/problems/path-sum/)| [Python3](Python3/BinaryTree/hasPathSum.py)|TODO:BFS,DFS||
|13|[Path Sum II](https://leetcode.com/problems/path-sum-ii/)| [Python3](Python3/BinaryTree/pathSumII.py)|TODO:BFS,参考链接在代码里|:octocat:|
|14|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)| [Python3](Python3/BinaryTree/kthSmallest.py)||:octocat:|
|15|[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)| [Python3](Python3/BinaryTree/flatten.py)|||
|16|[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)| [Python3](Python3/BinaryTree/Codec.py)||:octocat:|
|17|[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)| [Python3](Python3/BinaryTree/lowestCommonAncestor.py)|只是一颗普通的树TODO|:octocat:|
|18|[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)| [Python3](Python3/BinaryTree/lowestCommonAncestorBST.py)|||
|19|[Same Tree](https://leetcode.com/problems/same-tree/)| [Python3](Python3/BinaryTree/isSameTree.py)|||
|20|[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)| [Python3](Python3/BinaryTree/isSubtree.py)||:octocat:|
|21|二叉树的下一个节点| [Python3](Python3/BinaryTree/nextNode.py)|题目描述在代码内|:octocat:|
|22|二叉搜索树的后序遍历| [Python3](Python3/BinaryTree/isBST.py)|题目描述在代码内|:octocat:|
|23|二叉搜索树与双向链表| [Python3](Python3/BinaryTree/Convert.py)|题目描述在代码内；代码需要再理解一下|:octocat:|
|24|[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|[Python3](Python3/BinaryTree/maxPathSum.py)||:octocat:| 
|25|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|[Python3](Python3/BinaryTree/isValidBST.py)|||
|26|[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)|[Python3](Python3/BinaryTree/insertIntoBST.py)|||
|27|[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)|[Python3](Python3/BinaryTree/BSTIterator.py)|||
|28|[Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)|[Python3](Python3/BinaryTree/deleteNode.py)|||

[Back to Top](#index)



## Array

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Missing Number](https://leetcode.com/problems/missing-number/)| [C++](C++/Array/missingNumber.cpp)|||
|1|[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)| [Python3](Python3/Array/findDuplicate.py)|Solution 3**|:octocat:|
|2|[Find All Duplicate Number](https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/)| [Python3](Python3/Array/findAllDuplicate.py)||:octocat:|
|3|[My Calendar I](https://leetcode.com/problems/my-calendar-i/)| [Python3](Python3/Array/myCalendar.py)||G|
|4|[My Calendar II](https://leetcode.com/problems/my-calendar-ii/submissions/)| [Python3](Python3/Array/myCalendarII.py)|TODO:Soluton2|G|
|5|[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)| [Python3](Python3/Array/removeDuplicates.py)|也在two pointer里面||
|6|[80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)|[Python3](Python3/Array/removeDuplicatesII.py)|也在two pointer里面|| 
|7|[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|[Python3](Python3/Array/merge.py)|也在two pointer里面, add Follow up|| 
|8|[189. Rotate Array](https://leetcode.com/problems/rotate-array/)|[Python3](Python3/Array/rotate.py)||| 

[Back to Top](#index)




## String
 
|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Reverse String](https://leetcode.com/problems/reverse-string/)| [C++](C++/String/reverseString.cpp)|||
|1|[Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)| [Python3](Python3/String/numUniqueEmails.py)||G|
|2|[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|[Python3](Python3/String/reverseWords.py)|||

[Back to Top](#index)



## Linked List

|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)| [Python3](Python3/LinkedList/reverseList.py)||:octocat:|
|1|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [Python3](Python3/LinkedList/reverseBetween.py)|||
|2|[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|[Python3](Python3/linkedList/deleteDuplicates.py)|||
|3|[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|[Python3](Python3/linkedList/deleteDuplicatesII.py)|||
|4|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|[Python3](Python3/linkedList/mergeTwoLists.py)|||
|5|[Partition List](https://leetcode.com/problems/partition-list/)|[Python3](Python3/linkedList/partition.py)|||
|6|[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|[Python3](Python3/linkedList/removeElements.py)|||
|7|[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|[Python3](Python3/linkedList/middleNode.py)|||

[Back to Top](#index)


## BFS
|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|网格中走到某一位置的最短路径| [Python3](Python3/BFS/minPath.py)|题目要求在代码内|:octocat:|
|1|[Perfect Squares](https://leetcode.com/problems/perfect-squares/submissions/)| [Python3](Python3/BFS/numSquares.py)||:octocat:|
|2|[Word Ladder](https://leetcode.com/problems/word-ladder/)| [Python3](Python3/BFS/ladderLength.py)||:octocat:|

[Back to Top](#index)


## DFS
|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)| [Python3](Python3/DFS/maxAreaOfIsland.py)||:octocat:|
|1|[Number of Islands](https://leetcode.com/problems/number-of-islands/)| [Python3](Python3/DFS/numIslands.py)||:octocat:|
|2|[Friend Circles](https://leetcode.com/problems/friend-circles/)| [Python3](Python3/DFS/findCircleNum.py)||:octocat:|
|3|[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)| [Python3](Python3/DFS/solve.py)|BackTracking|:octocat:|
|4|[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)| [Python3](Python3/DFS/letterCombinations.py)|BackTracking|:octocat:|
|5|[46. Permutations](https://leetcode.com/problems/permutations/)| [Python3](Python3/DFS/permute.py)|BackTracking|:octocat:|
|6|[47. Permutations II](https://leetcode.com/problems/permutations-ii/)| [Python3](Python3/DFS/permuteII.py)|没想明白！BackTracking||
|7|[77. Combinations](https://leetcode.com/problems/combinations/)| [Python3](Python3/DFS/combine.py)|BackTracking,**TODO:**Solution 2||
|8|[78. Subsets](https://leetcode.com/problems/subsets/)| [Python3](Python3/DFS/subsets.py)|BackTracking||

||**TODO:**417,93,79,257,39

[Back to Top](#index)


## Dynamic Programming
|Idx|Questions|Solution|Info|Lable|
|---|--------|:-------:|:--------:|:-----:|
|0|[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)| [Python3](Python3/DP/lengthOFLIS.py)|TODO:O(nlogn)参考链接在代码里|:octocat:百度|
|1|[背包问题] | [Python3](Python3/DP/knapsack.py)|**0-1背包**题目描述在代码内|:octocat:|
|2|[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)| [Python3](Python3/DP/canPartition.py)|**0-1背包**|:octocat:|
|3|[Target Sum](https://leetcode.com/problems/target-sum/)| [Python3](Python3/DP/findTargetSumWays.py)|**0-1背包, TODO:DFS**|:octocat:|
|4|[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)| [Python3](Python3/DP/climbStairs.py)|斐波那契数列||

[Back to Top](#index)