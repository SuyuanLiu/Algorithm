# -*- coding:utf-8 -*-
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

