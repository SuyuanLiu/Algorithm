'''
@lsy 2019.11.8

还不是很懂，没心思理解，下次再看吧....
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
