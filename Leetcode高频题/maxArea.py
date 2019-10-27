'''
@lsy 2019.10.27

最大面积取决于两个边界中较小的一边。

Solution 1:
暴力，brute force， TLE(Time Limited Error)
i从0开始，j从i+1开始，找那个最大的面积即可。
时间复杂度O(n^2)

Solution 2:
双指针。
从两边往中间找，移动较小的那个边界。
时间复杂度O(n)
'''
# Solution 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                res = max(res, min(height[i], height[j])*(j-i))
        return res

# Solution 2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res