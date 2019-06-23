'''
解题思路：
Solution 1
- 利用求二叉树深度，每遍历到一个结点，就判断左右子树高度是否超过1
- 结点重复遍历

Solution 2
- 递归遍历，每个结点只遍历一遍
- 在判断二叉树高度时，如果当前子树不是平衡二叉树就返回-1，否则返回子树的高度

Test Cases：
- 平衡二叉树，非平衡二叉树，所有结点没有左结点/没有右结点
- 空树，只有一个结点

'''
# Solution 1
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return 1 + max(left, right)
     
    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        left = self.IsBalanced_Solution(root.left)
        right = self.IsBalanced_Solution(root.right)
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if left and right and abs(leftDepth - rightDepth) <= 1:
            return True
        return False

# Solution 2
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
     
    def IsBalanced_Solution(self, root):
        if not root:
            return True
        return self.depth(root) != -1
