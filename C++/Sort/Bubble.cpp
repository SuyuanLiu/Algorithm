/*
Solution:冒泡排序，时间复杂度O(n^2)，空间复杂度O(1);
- 每次遍历数组时，两两比较，把比较大的往后移，一轮下来最大的就排到了最后；
- 对数组做n-1次遍历；
*/
class Solution {
public:
    void sortIntegers(vector<int> &A) {
        if(! A.size())
            return ;
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A.size() - i - 1; j++){
                if(A[j] > A[j+1]){
                    int temp = A[j];
                    A[j] = A[j+1];
                    A[j+1] = temp;
                }
            }
        }
    }
};