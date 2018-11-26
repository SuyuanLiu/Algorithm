/*
Solution:选择排序，时间复杂度O(n^2)，空间复杂度O(1);
- 每次遍历数组时，选出最小值放在最前面；
- 对数组做n-1次遍历；
*/
class Solution {
public:
    void sortIntegers(vector<int> &A) {
        if(not A.size())
            return ;
        for(int i = 0; i < A.size(); i++){
            int minIdx = i;
            for(int j = i + 1; j < A.size(); j++){
                if(A[j] < A[minIdx])
                    minIdx = j;
            }
            int temp = A[minIdx];
            A[minIdx] = A[i];
            A[i] = temp;
        }
    }
};