'''
解题思路：
借助辅助栈。用辅助栈模拟弹出序列的顺序。
- 读取popV的第一个元素，把pushV元素压入辅助栈，直到遇见popV的第一个元素
- 弹出辅助栈栈顶元素，判断此时辅助栈栈顶元素是否与下一个popV元素相同，相同继续弹出，不同的话继续把pushV元素入栈直到再次相同
- 如果一直入栈，直到最后一个元素，都没找到相同的，说明这个出栈顺序不对
可以举例操作一下。

Solution 2:
同一个思路，使用了pop(0)，pop(0)时间复杂度是O(n)

时空复杂度：
- 时间复杂度 O(n)
- 空间复杂度 O(n)

Test Cases：
- 两个数组都空，数组长度不同
- 只含一个元素，含有多个元素
- 不是对应都出栈顺序

⚠️
询问都空时该返回什么；
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        if len(pushV) != len(popV):
            return False
        
        s = [pushV[0]]
        i, j = 1, 0
        while s or i < len(pushV):
            if s[-1] != popV[j]:
                while s[-1] != popV[j]:
                    if i >= len(pushV):
                        return False
                    s.append(pushV[i])
                    i += 1
            s.pop()
            j += 1
        return True


# Solution 2

class Solution:
    def IsPopOrder(self, pushV, popV):
        s = []
        s.append(pushV.pop(0))
        while popV:
            if not s:
                s.append(pushV.pop(0))
            if popV[0] != s[-1]:
                if not pushV:
                    return False
                s.append(pushV.pop(0))
            else:
                s.pop()
                popV.pop(0)
        return True
