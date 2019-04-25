/*
Solution 1:
- 直接利用加法求和，n个整数的和为n*(n+1)/2,依次减去数组中的值即可；
- 但存在的问题是：数值有可能会很大，溢出；
- 改进：每次加和只加一个数就做减法；

Solution 2:
- 利用异或，一个数与本身异或是0，与0异或是本身；
- 先对数组中所有数字进行异或，然后再对这个值做1~n的异或，剩下的值就是缺的值；
*/

// Solution 1:
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0; i < nums.size(); i++){
            n = n + i - nums[i];
        }
        return n;
    }
};


// Solution 2:
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = 0;
        for(int i = 0; i < nums.size(); i++){
            n = n ^ nums[i];
        }
        for(int i = 0; i < nums.size()+1; i++){
            n = n ^ i;
        }
        return n;
    }
};