/*
Solution:双指针，时间复杂度O(n)，空间复杂度O(1).
- 参考Discuss排名第一的解法：
  https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
- 基本思路是：
  start固定，end往后走，找到一个包含所有t字符的窗口；
  然后缩短这个窗口，固定end，让start往后走，看start最多能走到哪里；
  重复以上操作；找到最短窗口；

- 设置长度为128的map，用来存放字符串t中每个字符出现的次数，count为t字符个数;
- 定义两指针start，end，都从0开始，固定start，end向后扫描，对map值做减1操作，如果出现t中值，count--；
  当count为0时，说明当前start--end窗口内包含所有t中字符，判断map[s[start]]是否为0，不为0说明start位置不是t中字符，可以向后移动，否则count++；继续寻找下一个符合条件的窗口；
- 这里边充分用到 b=a++ 这类操作，这个操作先做 b=a, 然后才是 a++;


- 说明：
    - 字符串t中是否允许出现重复字母，在面试时要主动与面试官沟通，这里可以自定义testcase看结果；
    - Discuss第一解答中，提供了一个关于substring的模板；
*/
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(128, 0);
        for(auto c : t)
            map[c]++;
        int start = 0, end = 0;
        int count = t.size();
        int minLen = INT_MAX;
        int idx = 0;
        while(end < s.size()){
            if(map[s[end++]]-- > 0)
                count--;
            while(count == 0){
                if(minLen > end-start){
                    minLen = end - start;
                    idx = start;
                }
                
                if(map[s[start++]]++ == 0)
                    count++;
            }
        }
        return minLen == INT_MAX ? "" : s.substr(idx, minLen);
    }
};