# Dynamic Programming

Outline
- [](#题目)
- [](#什么时候用DP)
- [](#DP的四个要素)
- [](#面试常见的四种类型)
- [](#)

## 题目

- https://leetcode.com/problems/triangle/
Traversal， divide and conquer （时间复杂度O（2^n））
记忆化搜索：对divide and conquer，做一个优化，保存之前的值，让每个点只展开一次，时间复杂度O(n^2)(一共是n层，点的个数是n^2级别)
记忆化搜索本质就是动态规划，是DP的一种递归的实现。  

DP：大问题-->小问题，解决重复计算的问题
（递归：大问题-->小问题，有重复的问题）
（二叉树每个子树都是独立的，不会有重复的，这道题目是有交叉的）

DP一般使用循环的方式实现，从底到上面，自底向上的DP（这道题也可以用自顶向下，但是会比较复杂）
时间复杂度O(n^2)，空间复杂度O(n^2)， 空间复杂度可以优化到O(n)。（因为第i层只与上一层的结果相关，i%2就行了，dp设置成一个2行的就行了）

## 什么时候用DP

- 最大最小，最长最短
- yes/no
- count（比如方案的个数等），如果让你列出所有方案，一定不是dp，用递归(eg，k Sum, k Sum II)

同时，满足这个条件（这个条件不是很重要）：给出的数据不让排序，调位置，can not sort/swap

（比如，longest consecutive sequence，给的是一个集合，集合随便换顺序，这个就不是DP）

## DP的四个要素

- 状态（最重要）
- 状态方程
- 初始状态
- 最终答案


## 面试常见的四种类型

- Matrix DP（10%）
- Sequence （40）
- Two Sequences DP （40）
- BackPack （10 ）  背包


### Matrix DP

很明显，会给出一个矩阵，六边形等，有坐标概念的。
state：dp[x][y]从xxx走到坐标x，y  
function：上一步到x，y
initial：起点（只要是二维的，有时要考虑一下dp[i][0],dp[0][i]的初始化）
answer：终点

- minumum path sum
- unique paths（给一个矩阵，只能向右走，向下走，有多少种方案），数学上有个计算公式(m+n)!/m!n!，面试先给出这个公式，然后再去给他写dp代码（这个公式跟dp关系不是很大吧，我觉得）
- unique path II（有些点被扣掉）

### Sequence

题目一般会给一个数组或者字符串

state：dp[i]表示前i个字符/字符/数字/，.... 
function：dp[i] = dp[j]..j是i之前的一个位置
initial：dp[0]
answer：dp[-1]

- climbing stairs
- jump game(这题最优的是贪心算法，可以用DP)
- jump game II(最优的是贪心算法，可用DP)
- palindrome partition II
- word segmentation
- longest increasing subsequence(LIS), subsequence可以不连续，sub...是连续的

### Two Sequences 

一般是给两个数组/字符串，去看他们的匹配关系。

- state：f[i][j]表示第一个sequence的前i个数字（字符）**配上**第二个sequence的前j个数字（字符）....
- function：f[i][j]研究第i个与第j个之间的关系
- initialize：第一行和第一列，f[0][i], f[i][0]
- answer: f[-1][-1]

注意，假设两个数组/字符串的长度分别为n，m，一般这个DP数组长度会设一个DP[n+1][m+1]，一般要留出第0个这个；

题目：
- longest common subsequence(LCS), 子序列不一定连续；要时候要return最长的子序列，DP也是能做的；
- longest common substring,子串一定要连续（或者可以用两层循环去做，普通第方法）
- Edit distance，把word1变为word2最少需要多少步（利用LCS即可，找到他们的最长子序列）/或者：直接用DP，上面最开始的方程（手机拍了照片）
- Distinct subsequence(照片)
- Interleaving string(照片), f[i][j]表示s1的前i个字符，s2的前j个字符能否组成s3的前i+j个字符；

### BackPack 背包

判断能否用动归，第二个条件，不能交换，这个条件，对背包来说不满足。背包问题很明显，一下子就能看出来。他有一个取和的过程。

- 背包问题（lintcode92）(照片)，二维数组，有一维表示和的形式；要么取这个商品，要么不取；时间复杂度O(nm),空间复杂度O(nm)，空间复杂度可以优化到O(m),因为第i仅与第i-1相关。
- 背包2（lintcode152）(照片)
- K sum（lintcode89）(照片)
- minimun adjustment cost(lintcode 91)(照片)


## 记忆化搜索

先把它写成分治的搜索，在return之前，把结果存起来，下次就不用算了，直接读取就好了（相当于一个cache的作用），traingel那题，本来2^n的复杂度，后面就会变成n^2的复杂度，就几乎变成DP了。（照片DFS）


## other

- 拓扑排序用来判断图里面是否有环


练习：
- wildcard matching(lintcode 192),可以用动归，但最快的不是动归，而是有限状态自动机（凡是匹配的，都是这个方法）