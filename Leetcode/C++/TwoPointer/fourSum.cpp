/*
Solution:
- 暴力解法，时间复杂度 O(n^4)(这边没给出具体解法，就是4个for循环嵌套)；
- 双指针，先对数组做一个排序，时间复杂度 O(n^3);
  与3Sum是一个解题思路，注意重复元素的判断，j > i+1... 
*/
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if(nums.size() < 4){
            return res;
        }
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 3; i++){
           if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i + 1; j < nums.size() - 2; j++){
               if(j > i + 1 && nums[j] == nums[j-1]){
                    continue;
                }
                int p = j + 1, q = nums.size() -1;
                while(p < q){
                    int s = nums[i] + nums[j] + nums[p] + nums[q];
                    if(s < target){
                        p++;
                    }
                    else if(s > target){
                        q--;
                    }
                    else{
                        vector<int> temp{nums[i], nums[j], nums[p], nums[q]};
                        res.push_back(temp);
                        while(nums[p] == nums[p+1]){
                            p++;
                        }
                        while(nums[q] == nums[q-1]){
                            q--;
                        }
                        p++; q--;
                    }
                }
            }
        }
        return res;
    }
};