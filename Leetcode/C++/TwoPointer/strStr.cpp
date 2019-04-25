/*
注意特殊情况的判断；
- 这边如果needle = ''的话，需要输出什么，最好跟面试官沟通一下；
- 如果 haystack.size() < needle.size(),直接return -1；
*/
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size() == 0){
            return 0;
        }
        if(haystack.size() < needle.size()){
            return -1;
        }
        for(int i = 0; i < haystack.size() - needle.size() + 1; i++){
            if(haystack.compare(i, needle.size(), needle) == 0){
                return i;
            }
        }
        return -1;
    }
};