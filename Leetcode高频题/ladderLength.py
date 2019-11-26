'''
@lsy 2019.11.26
BFS.
设置队列。放置word以及对应的路径长度。
从当前word出发，把所有可能的改变一个字母的word都放到队列里面去，直到出现endword。

Discuss里面的高票答案还不是很懂。
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        visited = set()
        while queue:
            word, cnt = queue.popleft()
            if word == endWord:
                return cnt
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList and next_word not in visited:
                        queue.append([next_word, cnt+1])
                        visited.add(next_word)
        return 0