/*
Solution：快排，时间复杂度O(nlogn)，空间复杂度O(1);
- 快排思想是在数组中随机选取一个数，把比它小的值放前面，比它大的放后面（partition过程）；
- 然后递归对这个数值的左右两侧再进行划分；
- 具体partition过程：
  随机选取一个数，把它放在数组最后面（一般直接选择最后一个数）；
  然后在数组最前面划出一块区域，专门放小的值；
  遍历数组，比选择值的大直接跳过，小的与那块区域后面的一个值进行交换；
*/
class Solution {
public:
    void quickSort(vector<int> &A, int start, int end){
        if(start >= end)
            return;
        int smaller = start;
        for(int i = start; i < end; i++){
            if(A[i] < A[end]){
                int temp = A[i];
                A[i] = A[smaller];
                A[smaller++] = temp;
            }
        }
        int temp = A[smaller];
        A[smaller] = A[end];
        A[end] = temp;
        
        quickSort(A, start, smaller-1);
        quickSort(A, smaller+1, end);
    } 
     
    void sortIntegers(vector<int> &A) {
        if(!A.size())
            return ;
        quickSort(A, 0, A.size()-1);
    }
};