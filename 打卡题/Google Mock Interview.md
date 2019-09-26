# Google Mock Interview

2019.9.22

**Index**

- [Number of Binary Tree](#Number-of-Binary-Tree)
- [Flood the World Map](#Flood-the-World-Map)
- [Practice](#Practice)

### Number of Binary Tree

Given a number n, give how many different binary tree can be using n nodes? For example:  
n = 2, res = 2
node node  
 / \
 node node

n = 3, res = 5
node node node node node
/ / / \ \ \
 node node node node node node
/ \ / \
 node node node node

Solution: 树的数目数 = left 数目数 \* right 数目数  
Solution 1: 递归，时间复杂度指数级别

```python
def treeNum(n):
  if n < 3:
    return n if n != 0 else 1

  res = 0
  for i in range(n):
    left = treeNum(i)
    right = treeNum(n-i-1)
    res += left * right

  return res
```

Solution 2: dp, dp[i] = sum(dp[k] \* dp[i-k-i])，时间复杂度 O(n^2)；下面代码有个小的优化，第二层循环可以降为一半时间复杂度。

```python
def treeNum(n):
  if n < 3:
    return n if n != 0 else 1

  dp = [1 for i in range(n+1)]
  dp[2] = 2

  for i in range(3, n+1):
    for k in range(i):
      dp[i] += dp[k] * dp[n-k-1]

  return dp[-1]
```

### Flood the World Map

Given a N x N grid world map. Numbers in the grid represents the height of the wall. In the left side of the grid, there is a river with height H. If H > grid[i][j], then grid[i][j] is flooded. Return another grid about the wall flood state.  
水流可以朝着上下左右四个方向。

Solution： dfs。在 grid 的第一列找到被淹的点，然后从这个点出发，去找其他与之相连的被淹没的点。连通域。或者用 bfs 也可以。时间复杂度是 O(n^2)，因为每个点最多被遍历一遍。

```python
def dfs(grid, flood, H, visited, posx, posy):
  position = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for i in range(4):
    x, y = posx + position[0], posy + position[1]
    if 0 <= x < N and 0 <= y < N and grid[x][y] < H and (x,y) not in visited:
      visited.append((x,y))
      flood[x][y] = True
      visited, flood = dfs(grid, flood, H, visited, x, y)
  return visited, flood

def floodWorld(grid, N, H):
  visited = []
  flood = [[False for j in range(N)] for i in range(N)]

  for i in range(N):
    if grid[i][0] >= H:
      break
    elif (i,0) not in visited:
      visited, flood = dfs(grid, flood, H, visited, i, j)
  return flood

```

**Follow up**: There is a person at (x,y), his cat is at (x2, y2). If this person wants to rescure his cat within K steps, what is the max height of river, return H.  
Solution: 二分，没太懂

### Practice

- [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)--> [code](shipWithinDays.py)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) --> [code](splitArray.py)
