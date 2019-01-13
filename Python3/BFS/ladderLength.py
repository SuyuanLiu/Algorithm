# -*- coding:UTF-8 -*-
'''
Solution:
- BFS
- 把各个单词看成是图中的点，两个单词间只相差一个单词的话，两个单词之间就有连线；
- 建立一个队列，存储每层遍历到的单词；对已经遍历过的单词做标记，比如清空；

Solution 1:
在Leetcode上代码测试不通过，超时了，代码逻辑没有问题。（Python语言的缘故）

Solution 2:
在Disscus页面，借助广大网友的思路，对代码做了如下改进，让代码跑的快一点。

'''
# Solution 2


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
        
        
        