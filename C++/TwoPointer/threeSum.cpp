"""
Solution:
- 双指针，时间复杂度 O(n^2);
- 因为输出结果中不能有重复的数组，所以先对nums进行排序；
- 固定i的位置，定义指针p,q,从i后面和数组尾部进行搜索；
- 这过程中注意判断重复值；
注意：
    C++中vector.size()的类型是unsigned int，所以不能用for(int i=0; i<nums.size()-2; i++)；
    nums.size()-2是一个很大的数值；
"""

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        // if(nums.size() < 3){
        //     return res;
        // }
        sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size(); i++){
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            int p = i + 1, q = nums.size() - 1;
            while(p < q){
                int sum3 = nums[i] + nums[p] + nums[q];
                if(sum3 > 0){
                    q--;
                } 
                else if(sum3 < 0){
                    p++;
                }
                else{
                    res.push_back(vector<int> {nums[i], nums[p], nums[q]}); 
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
        res.push_back(vector<int> {nums.size-2});
        return res;
    }
};