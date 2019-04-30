# Graph & Search

Graph
- clone graph (copy list with random pointer)
- topological sorting

Search
- DFS
- BFS

## Graph

关于图的克隆(clone graph)，分为两个步骤：克隆点，克隆边。注意克隆点，要把新生成的点和之前的点做一个关联，用map/dic即可。关于图结点的遍历，推荐使用BFS. DFS也可以，只不过是在大多数情况下，BFS有个模板可以套用。

关于拓扑排序(Topological Sort)，就是从入度为0的结点开始，找到入度为0的结点之后，把入度为0的结点及它所对应的关系给删掉，接着寻找入度为0的点。(判断图是否有环也是这个思想，删除入度为0的点，直到全部删完，如果最后还有点，那么就是成环了。)



## Search

当要求给出所有的可能解的时候，应该考虑到DFS。   
DFS的两个根本问题：permutation，subsets

关于DFS：当题目中出现find all possible subsets/cases...，考虑使用DFS。可以画出搜索树，辅佐分析，叶子结点是结果还是说所有的结点都是结果。

例题：
- permutation，给出所有排列顺序的组合
- subsets，给出序列的所有子集




