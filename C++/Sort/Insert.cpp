/*
Solution:插入排序，时间复杂度O(n^2)，空间复杂度O(1);
- 假设前i个元素有序，将第i+1个元素依次与前面元素比较，插入到合适的位置；
- 因为前i个元素有序，所以当A[i] < A[i+1]时，就不用再遍历。
*/

class Solution {
public:
    void sortIntegers(vector<int> &A) {
        if(not A.size())
            return ;
        for(int i = 0; i < A.size() - 1; i++){
            for(int j = i + 1; j > 0; j--){
                if(A[j] < A[j-1]){
                    int temp = A[j];
                    A[j] = A[j-1];
                    A[j-1] = temp;
                }
                else
                    break;
            }
        }
    }    
};