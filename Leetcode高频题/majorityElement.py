'''
@lsy 2019.12.20

用num，cnt分别记录当前数字，以及出现次数。
遍历数组，若当前数字与num不同，cnt - 1；否则加1；若cnt变为0，则更换num为当前数字。最后的num就是出现超过一半的num。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, cnt = None, 0
        
        for n in nums:
            if cnt == 0:
                num, cnt = n, 1
            elif n != num:
                cnt -= 1
            else:
                cnt += 1
                
        return num