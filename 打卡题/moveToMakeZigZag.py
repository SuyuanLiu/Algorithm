'''
@lsy  2019.9.18
贪心

注意题目要求，只能下调数字。如果也可以上调的话，就是dp了（不懂）
注意追踪应当为小值的位置上的数值。如果这个位置的值比较大，就应当下调这个值。
两种情况：
- 奇数位置为大值
- 偶数位置为大值
视频讲解：https://www.youtube.com/watch?v=SD99cAHkRow（还是有些晕）
'''
class Solution: 
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        cnt_odd, cnt_even = 0, 0
        _max = 0
        
        # odd: small big small big small ...
        for i in range(0, len(nums), 2):   
            if i == 0:
                _max = nums[i+1]
            elif i == len(nums) - 1:
                _max = nums[i-1]
            else:
                _max = min(nums[i-1], nums[i+1])
            if nums[i] >= _max:
                cnt_odd += nums[i] - _max + 1
                
        # even: big small big small ...
        for i in range(1, len(nums), 2):
            if i == len(nums) - 1:
                _max = nums[i-1]
            else:
                _max = min(nums[i-1], nums[i+1])
            if nums[i] >= _max:
                cnt_even += nums[i] - _max + 1
        
        return min(cnt_odd, cnt_even)
