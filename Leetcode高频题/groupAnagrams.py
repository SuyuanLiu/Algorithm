'''
@lsy 2019.11.11

使用字典。
dic.get(key, [])，作用是在dic中寻找key对应的键值，找不到则返回 []
使用tuple原因：sorted(str)后得到的是list，非hash，不能用作字典的key，使用tuple后，可用作字典key。
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return list(dic.values())
