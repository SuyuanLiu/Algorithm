'''
@lsy 2019.10.21

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, n in enumerate(nums):
            num = target - n
            if num in dic.keys():
                return [i, dic[num]]
            else:
                dic[n] = i
                