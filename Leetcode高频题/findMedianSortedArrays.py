'''
@lsy, 2019.10.21

这题好难🤯啊，边界也容易出错。
Solution：
二分法。
假设nums1是比较短的那个数组。
如果在nums1中已经指定了划分点，那么nums2中的划分点也就确定。
在划分点确定后，需要确保划分点左侧所有点都小于划分点右侧的点。（自己画图演示）
也就是要maxLeftX <= minRightY and maxLeftY <= minRightX
如果 maxLeftX > minRightY，说明需要将nums1的划分点向左移动
如果 maxLeftY > minRightX，说明需要将nums1的划分点向右移动

特殊情况：
当某个数组左侧的点为空，需要设置为-float('inf')
如果右侧为空，需要设置为float('inf')

注意边界条件：
end是从L1开始，而不是L1 - 1
while 判断停止的条件是 start <= end
nums1[p1 - 1]
start = p1 + 1
end = p1 - 1

时间复杂度O(log(min(m,n)))，空间复杂度O(1)

好像有个把他变为寻找第K大的数，更通用化。那么中点就是找第 (n+m)/2 大的数（数组总长度为偶数）。
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L1, L2 = len(nums1), len(nums2)
        if L1 > L2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        L1, L2 = len(nums1), len(nums2)
        start, end = 0, L1 
        while start <= end:
            p1 = (start + end) // 2
            p2 = (L1 + L2 + 1) // 2 - p1
            
            maxLeftX = nums1[p1-1] if p1 != 0 else -float('inf')
            minRightX = nums1[p1] if p1 != L1 else float('inf')
            
            maxLeftY = nums2[p2-1] if p2 != 0 else -float('inf')
            minRightY = nums2[p2] if p2 != L2 else float('inf')
            
            if maxLeftX > minRightY:
                end = p1 - 1
            elif maxLeftY > minRightX:
                start = p1 + 1
            else:
                if (L1 + L2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
