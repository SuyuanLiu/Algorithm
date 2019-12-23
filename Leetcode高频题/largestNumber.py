'''
@lsy 2019.12.23

实现一个比较函数，对数组进行排序。
注意下面sort中对比较函数的使用，若直接令 key=compare，会报错，报b不存在；
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        
        compare = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = list(map(str, nums))
        import functools 
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)