'''
Solution:
- 非递归和递归
- 主要思想：将target与数组中间的值进行比较，target == nums[mid], 则返回对应下标；
                                        target > nums[mid]， 说明只能在右侧寻找；
                                        target < nums[mid]， 说明只能在右侧寻找；
- 时间复杂度：O(logN), 递归算法额外使用了栈的信息；
'''

// Solution 1: iterative
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(!nums.size())
            return -1;
        int start = 0, end = nums.size() - 1;
        while(start <= end){
            int mid = (start + end) / 2;
            if(target < nums[mid])
                end = mid - 1;
            else if (target > nums[mid])
                start = mid + 1;
            else
                return mid;
        }
        return -1;
    }
};

// Solution 1: recursive
class Solution {
public:
    int binarySearch(vector<int> &nums, int start, int end, int target){
        if(start > end)
            return -1;
        int mid = (start + end) / 2;
        if(target < nums[mid])
            end = mid - 1;
        else if(target > nums[mid])
            start = mid + 1;
        else
            return mid;
        return binarySearch(nums, start, end, target);
    }
    
    int search(vector<int>& nums, int target) {
        if(!nums.size())
            return -1;
        return binarySearch(nums, 0, nums.size(), target);
    }
};