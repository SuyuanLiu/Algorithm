/*
Solution: 双指针，时间复杂度O(n),空间复杂度O(1)
- 定义两个指针p,q分别指向字符串开始于结尾；
- 用isalnum判断是否为字母数字，否则指针右移或左移；
- 用toupper来判断大小写字母；
*/

class Solution {
public:
	bool isPalindrome(string s) {
		if (s == "")
			return true;

		int p = 0, q = s.size() - 1;
        while(p < q){
            while(!isalnum(s[p]) && p < q)   p++;
            while(!isalnum(s[q]) && p < q)   q--;
            if(toupper(s[p]) != toupper(s[q]))  
                return false;
            else{
                p++; q--;
            }
        }
        return true;
        
	}
};