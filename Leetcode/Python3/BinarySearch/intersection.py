# -*- coding:UTF-8 -*-
'''
Solution:
    - 使用字典，遍历第一个数组，把出现过的数字放进数组，并赋key=1;
    - 遍历第二个数组，如果字典中出现这个数字，并且key=1，加入ans,并且key=2;
'''

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        if not m or not n:
            return []
        dic, ans = {}, []
        for i in range(m):
            temp = nums1[i]
            if not dic.get(temp):
                dic[temp] = 1
        for i in range(n):
            temp = nums2[i]
            if dic.get(temp) == 1:
                ans.append(temp)
                dic[temp] = dic.get(temp) + 1
                
        return ans
            