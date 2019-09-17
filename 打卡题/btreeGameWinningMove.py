'''
@lsy  2019.9.16
这道题目首先要理解题意，然后想清楚，做起来就不难了。是一个简单的递归。
题目：
  给定一颗二叉树，palyer1选定一个点后，问第二个玩家是否能赢。
  实际上是看选定点后，能控制多少个其余的点。
  玩家2选的点一定得是玩家1点的邻居，即parent，left，right中的一个；
  选中一个点后，实际上就控制了其他的点。只要判断parent，left，right中控制点数更多的那个是否超过n/2即可。
具体讲解可参考：https://www.bilibili.com/video/av62548558
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def nodeNum(self, root):
        if not root:
            return 0
        L = self.nodeNum(root.left)
        R = self.nodeNum(root.right)
        return L + R + 1
    
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.val == x:
                L = self.nodeNum(node.left)
                R = self.nodeNum(node.right)
                Parent = n - L - R - 1
                return max([L, R, Parent]) > n // 2
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
