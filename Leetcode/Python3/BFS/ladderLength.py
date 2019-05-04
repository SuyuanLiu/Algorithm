# -*- coding:UTF-8 -*-
'''
Solution: BFS

Solution 1:
在Leetcode上代码测试不通过，超时了，代码逻辑没有问题。（Python语言的缘故）
- 把各个单词看成是图中的点，两个单词间只相差一个单词的话，两个单词之间就有连线；
- 建立一个队列，存储每层遍历到的单词；对已经遍历过的单词做标记，比如清空；

Solution 2:
参考这位朋友的代码：https://leetcode.com/problems/word-ladder/discuss/40810/Python-BFS-solution
代码能够通过leetcode测试了。
- 对当前单词，对它只改变一个字母，看改变后的单词是否在wordList里面，在的话，这两个单词之间就存在连线；
- 对已经遍历过的单词进行标记，放到visited里面去；
- 这边把wordList和visited都变成set，是哈希结构，访问查找时间复杂度是O(1)，可以提高速度；

说明：
这题是一道简单图的最短路径问题，所谓简单图就是指各条边的长度算作是1.求解这个题目，只能用BFS，每个结点遍历一遍，时间复杂度是O(n)，如果使用DFS，时间复杂度是O(2^n)，太大了。
'''
# Solution 2
import string


class Solution:  
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0
        
        wordList = set(wordList)       
        stack = [(beginWord, 1)]
        visited = set()
        while stack:
            word, cnt = stack.pop(0)
            if word == endWord:
                return cnt
            for i in range(len(word)):
                for c in string.ascii_lowercase:   # for c in 'abcdefghijklm....xyz'
                    tmp = word[:i] + c + word[i+1:]
                    if tmp not in visited and tmp in wordList:
                        stack.append((tmp, cnt+1))
                        visited.add(tmp)
                        
        return 0

# Solution 1
class Solution:
    def canChange(self, s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        return True if cnt == 1 else False
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0
        
        stack = [beginWord]
        cnt = 2
        
        while stack:
            for i in range(len(stack)):
                cur = stack.pop(0)
                for j in range(len(wordList)):
                    if wordList[j] and self.canChange(cur, wordList[j]):
                        if wordList[j] == endWord:
                            return cnt
                        stack.append(wordList[j])
                        wordList[j] = ''
            cnt += 1
        return 0
