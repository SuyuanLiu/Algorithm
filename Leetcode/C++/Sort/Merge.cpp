/*
Solution: 归并排序，时间复杂度O(nlogn),空间复杂度O(n);
- 思想就是，让数组左边独自有序，右边独自有序，然后合并左右两部分；
- 递归使得数组左右有序；
（归并就是每个单独的数，把他们两两相邻合并有序，然后再把这些小数组相邻的合并有序）
*/
class Solution {
public:
	void merge(vector<int> &A, int start, int end) {
		int mid = (start + end) / 2;
		int i = start, j = mid + 1;
		vector<int> B;
		int n = 0;
		while (i <= mid && j <= end) {
			if (A[i] < A[j])
				B.push_back(A[i++]);
			else
				B.push_back(A[j++]);
		}
		while (i <= mid)
			B.push_back(A[i++]);
		while (j <= end)
			B.push_back(A[j++]);
		for (int m = 0; m < B.size(); m++) {
			A[start++] = B[m];
		}
	}

	void mergeSort(vector<int> &A, int start, int end) {
		if (start >= end)
			return;
		int mid = (start + end) / 2;
		mergeSort(A, start, mid);
		mergeSort(A, mid + 1, end);
		merge(A, start, end);
	}

	void sortIntegers(vector<int> &A) {
		// write your code here
		if (!A.size())
			return;

		mergeSort(A, 0, A.size() - 1);
	}
};