# -*- coding:UTF-8 -*-
'''
Solution 1: 暴力解法，时间复杂度O(n)
- 把已经book的时间存到booktime里面
- 新的时间与booktime中每一个时间段进行比较，看是否重叠：
    新的start在booktime的时间段内；
    booktime时间段的开始时间在start，end之间；

Solution 2: Binary Tree, 时间复杂度O(logn)
- 建立一棵二叉搜索树，左节点 < 根节点 < 右节点，这边节点值指的是整个的时间段都小于或大于另一个节点值；
- 新插入节点[start, end]与[s,e]比较，如果start >= e，到树的右侧去找；如果 end <= s，到树的左侧去找，否则就是重叠了；
'''

# Solution 2
class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e 
        self.left = None
        self.right = None
    
    def insert(self, start, end):
        if start >= self.e:
            if self.right == None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        elif end <= self.s:
            if self.left == None:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        else:
            return False


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root == None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



# Solution 1
class MyCalendar:

    def __init__(self):
        self.booktime = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in range(len(self.booktime)):
            s, e = self.booktime[i]
            if start <= s < end or s <= start < e:
                return False
        
        self.booktime.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)