/*
Solution:
- 利用双指针思想，采用滑动窗口；时间复杂度O(n).
- 利用字典来存储字符出现过的位置，设置左右指针i,j分别指向子串的左右边界；
- 当j所指向字符不在i-j之间出现，j右移,如果出现这个字符，那么i右移，这个新的子串从重复字符出现位置的后面一个位置开始；并判断maxLen与j-i的大小；
- 关于字符是否出现用dict[s[j]] >= i来判断，dict[s[j]]表示j所指向字符最近一次出现的位置；
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() == 0){
            return s.length();
        }
        vector<int> dict(256, -1);
        dict[s[0]] = 0;
        int maxLen = 1, i = 0, j = 1;
        while(i <= j && j < s.length()){
            if(dict[s[j]] >= i){
                maxLen = max(maxLen, j-i);    
                i = dict[s[j]] + 1;
            }
            else{
                dict[s[j]] = j;
                j++;
            }
            if(i == j){
                dict[s[i]] = i;
                j++;
            }
        }
        maxLen = max(maxLen, j-i);
        return maxLen;
    }
};