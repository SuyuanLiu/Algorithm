'''
@lsy 2019.12.03

代码讲解参考: https://zhuanlan.zhihu.com/p/57733537

LRU
- Least Recent Used，最近最少使用缓存机制
- 当缓存容量超过上限，要删除那些最近最少使用的数据；也就是删除最长时间未使用的数据；
- 使用哈希表，同时希望使用有序的哈希表，按照插入顺序排放数据；
    在哈希表前面部分的数据是比较长时间存在的数据，在最后的数据是最新出现的数据，也就是最近使用过的数据；
    因此在插入数据时，如果插入的数据 key 已经存在，就要把这个 key-value 移动到哈希表的最后面；
- LRU 支持获取数据 get 和写入数据 put
    - get：若 key 在缓存中，则返回其对应的 value；否则返回 -1
    - put：若 key 不存在，则写入；否则需要把该 key-value移动到最后面（最新使用的）

注意：
python 中有有序哈希表，对于已经出现过的key，不会再次去调整顺序，所以要自己去实现这个。
（java中的 LinkedHashMap 会去调整顺序的）
'''
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self._ordered_dict = OrderedDict()
        self._capacity = capacity
        

    def get(self, key: int) -> int:
        self._move_to_end_if_exist(key)
        return self._ordered_dict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self._move_to_end_if_exist(key)
        self._ordered_dict[key] = value
        
        if len(self._ordered_dict) > self._capacity:
            self._ordered_dict.popitem(last=False)
            
    def _move_to_end_if_exist(self, key):
        if key in self._ordered_dict:
            self._ordered_dict.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)