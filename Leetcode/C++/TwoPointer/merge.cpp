/*
Solution:双指针，时间复杂度O(n),空间复杂度O(1)
- nums1长度足够大，把nums1中的数往后移，空出n个位置来；
- 定义两个指针p,q,分别指向nums1和nums2中的数值，比较大小即可；
*/
class Solution {
public:
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

		if (n != 0) {
			for (int i = m + n - 1; i >= n; i--) {
				nums1[i] = nums1[i-n];
			}
			int p = 0, q = n, i = 0;
			while (p < n && q < (m + n)) {
				if (nums2[p] < nums1[q]) {
					nums1[i++] = nums2[p++];
				}
				else {
					nums1[i++] = nums1[q++];
				}
			}
			while (p < n) {
				nums1[i++] = nums2[p++];
			}
			while (q < (m + n)) {
				nums1[i++] = nums1[q++];
			}
		}
	}
};