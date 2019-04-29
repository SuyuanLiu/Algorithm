'''
Solution 1:
- 🤔子集，从第1个元素开始，把第1个元素加入path，接着遍历后面的元素，path里面的内容要全部加上当前元素。
  比如[1,2,3],从1开始，path=[1],然后遍历[2,3]，遍历到2时，path=[[1],[1,2]],再遍历到3时，path=[[1],[1,2],[1,3],[1,2,3]]
  类似的接着从2开始...
- 时间复杂度 O(n^2), 空间复杂度 O(n)(这个时间复杂度不是很确定，子集的结果数是2^n，我感觉像是n^2)

Solution 2: DFS
- 时间复杂度 O(2^n),对于每个元素都有选择和不选择两种情况
- ⚠️注意：dfs函数内，不能用res.append(subset)，这样加入的subset就全部都是一个subset，最后subset又全部变为空。
'''
# Solution 2: DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], 0, res)
        return res
        
        
    def dfs(self, nums, subset, start, res):
        # res.append(subset)
        res.append([c for c in subset])
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, i+1, res)
            subset.pop()
            
            


# Solution 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res
    
        for i in range(len(nums)):
            path = [[nums[i]]]
            for j in range(i+1, len(nums)):
                path = path + [n + [nums[j]] for n in path]
            res += path
        
        return res
