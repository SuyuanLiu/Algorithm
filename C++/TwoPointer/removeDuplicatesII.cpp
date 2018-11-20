/*
Solution 1: 双指针，时间复杂度O(n),空间复杂度O(1)
- 定义指针i,j，j从前向后遍历数组，i指向当前无重复元素子数组的最后一个位置；
- 由于数组中允许最多出现两次同样的数字，所以再第一次遇到相同的数字时，要把第二个同数字移到前面去；

Solution 2：参考高票答案https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby
- 还是双指针的思想
- 定义i,n, i指向当前无重复子数组最后位置的后面一位，n为当前正在遍历的值；
- i < 2 时，满足最多两个重复值，n > nums[i-2]跨度为1，使得满足最多两个重复值；
*/

// ------- Solution 1 -------
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() < 3)  return nums.size();
        int i = 0, j = 1;
        while(j < nums.size()){
            if(nums[i] == nums[j]){
                nums[i+1] = nums[i];
                j++; i++;
            }
            while(j < nums.size() && nums[i] == nums[j])
                j++;
            if(j < nums.size())
                nums[++i] = nums[j++];
        }
        return i+1;
    }
};

// ------- Solution 2 -------
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() < 3)     
            return nums.size();
        int i = 0;
        for(int n : nums){
            if(i < 2 || n > nums[i-2])
                nums[i++] = n;
        }
        return i;
    }
};