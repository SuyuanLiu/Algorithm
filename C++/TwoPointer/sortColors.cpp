/*
Solution：双指针，时间复杂度O(n)，空间复杂度O(1)
- 设置指针p, q分别指向0区的最后一个位置和2区的第一个位置；
- 遍历数组，如果当前值为0，与nums[++p] 进行互换；如果为2，与nums[--q] 互换；为1的话，不进行操作；
- 注意当nums[i]等于2时，没有进行i++的操作，因为后面的数值被换到前面去，要对这个换过去的数值重新检查；
*/
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int p = -1, q = nums.size();
        int i = 0;
        while(i < q){
            if(nums[i] == 0){
                nums[i] = nums[++p];
                nums[p] = 0;
                i++;
            }
            else if(nums[i] == 2){
                nums[i] = nums[--q];
                nums[q] = 2;
            }
            else    i++;
        }
    }
};