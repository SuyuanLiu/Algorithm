/*
Solution 1: 
- 暴力解法，时间复杂度 O(n^3);

Solution 2:
- 双指针，对数组先做一个排序，时间复杂度 O(n^2)
- 排序之后，设置三个指针 i,p=i+1, q=nums.size()-1;
- 固定 i, 当三个数字之和小于target，说明该右移p；如果大于target，该左移q；相等的话直接return target；
- 要设置diff来记录最小差值；
*/

// Solution 1
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int diff = INT_MAX, sumClosest = 0;
        for(int i = 0; i + 2 < nums.size(); i++){
            for(int j = i + 1; j + 1 < nums.size(); j++){
                for(int k = j + 1; k < nums.size(); k++){
                    int temp = nums[i] + nums[j] + nums[k];
                    if(abs(target - temp) < diff){
                        diff = abs(target - temp);
                        sumClosest = temp;
                    }
                }
            }
        }
        return sumClosest;
    }
};

// Solution 2
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int diff = INT_MAX, sumClosest;
        for(int i = 0; i + 2 < nums.size(); i++){
            int p = i + 1, q = nums.size() - 1;
            while(p < q){
                int temp = nums[i] + nums[p] + nums[q];
                if(abs(target - temp) < diff){
                    diff = abs(target - temp);
                    sumClosest = temp;
                }
                if(temp < target){
                    p++;
                }
                else if(temp > target){
                    q--;
                }
                else{
                    return target;
                }
            }
        }
        return sumClosest;
    }
};